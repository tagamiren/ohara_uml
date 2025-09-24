import json
import os
from urllib.parse import parse_qs
import datetime

ROBODOG_FILE = "robodog.json"

def save_name(name):
    """名前をJSONに保存"""
    with open(ROBODOG_FILE, "w", encoding="utf-8") as f:
        json.dump({"name": name}, f, ensure_ascii=False)

def load_name():
    """JSONから名前を読み出す。なければ空文字"""
    if not os.path.exists(ROBODOG_FILE):
        return ""
    try:
        with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("name", "")
    except (json.JSONDecodeError, OSError):
        return ""
def get_greeting():
    """時刻に応じた挨拶を返す"""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 11:
        return "おはよう"
    elif 11 <= hour < 18:
        return "こんにちは"
    else:
        return "こんばんは"


def parse_post(environ):
    """POSTデータを辞書で返す"""
    try:
        request_body_size = int(environ.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0

    body = environ["wsgi.input"].read(request_body_size).decode("utf-8")
    return parse_qs(body)


def render_template(path, **kwargs):
    """テンプレートを読み込み、変数を埋め込み"""
    with open(path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)
