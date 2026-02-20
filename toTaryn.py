import requests
from config import *

def send_line_message(channel_access_token, message):

    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}",
    }
    data = {
        "messages": [{"type": "text", "text": message}],
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code != 200:
        print('request error')


send_line_message(LINE_CHANNEL_ACCESS_TOKEN, "hello taryn")
