from seleniumbase import SB
import time
import argparse
from config import *
from line_notify import send_line_message
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("--print", action="store_true")
parser.add_argument("--check", action="store_true")
args = parser.parse_args()

with SB(uc=True) as sb:

    sb.uc_open_with_reconnect(LOGIN_URL, reconnect_time=RECONNECT_TIME)
    time.sleep(WAIT_TIME * 2)

    sb.type(SELECTORS["username_input"], USERNAME)
    sb.type(SELECTORS["password_input"], PASSWORD)

    sb.wait_for_element_clickable(SELECTORS["submit_btn"], timeout=ELEMENT_TIMEOUT)
    sb.click(SELECTORS["submit_btn"])
    time.sleep(WAIT_TIME)
    
    sb.wait_for_element_clickable(SELECTORS["continue_btn"], timeout=ELEMENT_TIMEOUT)
    sb.click(SELECTORS["continue_btn"])
    time.sleep(WAIT_TIME)

    sb.open(COURSE_QUERY_URL)
    time.sleep(WAIT_TIME)

    sb.wait_for_element_visible(SELECTORS["subject_select"], timeout=ELEMENT_TIMEOUT)
    sb.select_option_by_value(SELECTORS["subject_select"], COURSE_CATEGORY_CODE)
    time.sleep(WAIT_TIME)

    sb.wait_for_element_clickable(SELECTORS["submit_query"], timeout=ELEMENT_TIMEOUT)
    sb.click(SELECTORS["submit_query"])
    time.sleep(WAIT_TIME)


    
    html = sb.get_page_source()
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one(SELECTORS["result_table"])
    rows = table.select("tr")

    total_courses = len(PICK_COURSE_CODE)
    results = []



    for row in rows:
        if len(results) >= total_courses:
            break
        cells = row.find_all("td")
        if not cells or len(cells) <= max(PICK_COLUMNS) or cells[4].get_text(strip=True) not in PICK_COURSE_CODE:
            continue

        if args.check:
            try:
                if int(cells[14].get_text(strip=True)) <= 0:
                    continue
            except ValueError:
                continue

        cell_texts = [cells[i].get_text(strip=True) for i in PICK_COLUMNS if i < len(cells)]
        cell_texts[1] = cell_texts[1].split(" ")[0]

        line = " | ".join(cell_texts)
        results.append(line)
        print(f"{len(results)}/{total_courses}", end='\r')


    if args.print:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(results))
    else:
        if results:
            msg = "hello Taryn:\n\n" + "\n".join(results)
            send_line_message(LINE_CHANNEL_ACCESS_TOKEN, msg)
        elif not args.check:
            send_line_message(LINE_CHANNEL_ACCESS_TOKEN, "no result")
