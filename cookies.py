import json, os
from config import LOGIN_URL

def save_cookies(sb):
    cookies = sb.get_cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

def load_cookies(sb):
    with open("cookies.json", "r") as f:
        cookies = json.load(f)