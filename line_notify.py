import requests

def send_line_message(channel_access_token, user_id, message):

    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}",
    }
    data = {
        "to": user_id,
        "messages": [{"type": "text", "text": message}],
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code != 200:
        print('request error')
