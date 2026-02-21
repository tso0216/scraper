from dotenv import load_dotenv
import os

load_dotenv()

# env
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

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
    "result_table": "table#myTable01 tbody",
}

COURSE_CATEGORY_CODE = "EFGKM"  # all通識課程
OUTPUT_FILE = "result.txt"
PICK_COLUMNS = [4, 5, 14]
PICK_COURSE_CODE = ['0214', '0233', '0234', '0256', '0280', '0529', '0530', '0640', '0690', '0106', '0109']

# 0214 | 數位輔助：英語看世界Hello | 0
# 0233 | 職涯規劃與成就自我Career | 0
# 0234 | 職涯規劃與成就自我Career | 0
# 0256 | 趣味生技與醫學應用Fun | 0
# 0280 | 生成式AI與ChatGPT應用Applications | 0
# 0529 | 生命的動力與延續The | 0
# 0530 | 生命的動力與延續The | 0
# 0640 | 人際關係與溝通Interpersonal | 0
# 0690 | 人際關係與社會互動Interpersonal | 0
# 0106 | 太極拳基礎Basic | 夜校
# 0109 | 社會心理學Social | 夜校 