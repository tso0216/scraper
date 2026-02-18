from dotenv import load_dotenv
import os

load_dotenv()

# env
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

# URL
LOGIN_URL = "https://ccidp.nchu.edu.tw/login"
COURSE_QUERY_URL = "https://cportal.nchu.edu.tw/cofsys/plsql/crseqry_gene_now"

# 等待時間
WAIT_TIME = 0.1
RECONNECT_TIME = 4
ELEMENT_TIMEOUT = 10

SELECTORS = {
    "username_input": "input#username",
    "password_input": "input#password",
    "submit_btn": '[name="submitBtn"]',
    "continue_btn": '[name="continue"]',
    "course_link": 'a[href*="crseqry_home"]',
    "subject_select": 'select[name="p_subject"]',
    "submit_query": 'input[type="submit"]',
    "result_table": "table#myTable01 tbody tr",
}

COURSE_CATEGORY_CODE = "EFGKM"  # all通識課程
OUTPUT_FILE = "result.txt"
PICK_COLUMNS = [4, 5, 14]
PICK_COURSE_CODE = ['0201', '0212', '0213']
