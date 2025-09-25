from urllib.parse import parse_qs


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
