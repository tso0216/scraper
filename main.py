from seleniumbase import SB
import time
from config import *

with SB(uc=True) as sb:
    # 登入
    sb.uc_open_with_reconnect(LOGIN_URL, reconnect_time=RECONNECT_TIME)
    time.sleep(WAIT_TIME * 2)

    sb.type(SELECTORS["username_input"], USERNAME)
    sb.type(SELECTORS["password_input"], PASSWORD)

    sb.wait_for_element_clickable(SELECTORS["submit_btn"], timeout=ELEMENT_TIMEOUT)
    time.sleep(WAIT_TIME)
    sb.click(SELECTORS["submit_btn"])

    sb.wait_for_element_clickable(SELECTORS["continue_btn"], timeout=ELEMENT_TIMEOUT)
    time.sleep(WAIT_TIME)
    sb.click(SELECTORS["continue_btn"])
    time.sleep(WAIT_TIME)

    # 導航至課程查詢
    sb.wait_for_element_clickable(SELECTORS["course_link"], timeout=ELEMENT_TIMEOUT)
    sb.click(SELECTORS["course_link"])
    sb.open(COURSE_QUERY_URL)
    time.sleep(WAIT_TIME)

    # 選擇通識課程並送出查詢
    sb.wait_for_element_visible(SELECTORS["subject_select"], timeout=ELEMENT_TIMEOUT)
    sb.select_option_by_value(SELECTORS["subject_select"], COURSE_CATEGORY_CODE)
    time.sleep(WAIT_TIME)

    sb.wait_for_element_clickable(SELECTORS["submit_query"], timeout=ELEMENT_TIMEOUT)
    sb.click(SELECTORS["submit_query"])
    time.sleep(WAIT_TIME)

    # 爬取結果並輸出
    rows = sb.find_elements(SELECTORS["result_table"])
    total_courses = len(rows)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for idx, row in enumerate(rows):
            cells = row.query_selector_all("td")
            if not cells:
                continue
            cell_texts = [cells[i].text for i in PICK_COLUMNS if i < len(cells)]
            line = " | ".join(cell_texts)
            f.write(line + "\n")
            print(f"{idx + 1}/{total_courses}",end='')

    time.sleep(5)
