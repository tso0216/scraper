from seleniumbase import SB
import time
from config import *

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
    
    rows = sb.find_elements(SELECTORS["result_table"])
    total_courses = len(PICK_COURSE_CODE)
    idx = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for row in rows:
            if idx >= total_courses:
                break

            cells = row.query_selector_all("td")

            if not cells or cells[4].text not in PICK_COURSE_CODE:
                continue
     
            cell_texts = [cells[i].text for i in PICK_COLUMNS if i < len(cells)]
            line = " | ".join(cell_texts)
            f.write(line + "\n")
            print(f"{idx + 1}/{total_courses}",end='\r')
            idx += 1
