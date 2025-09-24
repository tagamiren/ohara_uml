from wsgiref.simple_server import make_server
from app_logic import save_name, load_name, get_greeting, parse_post, render_template


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ["REQUEST_METHOD"]
    headers = [("Content-Type", "text/html; charset=utf-8")]

    if path == "/":
        body = render_template("templates/menu.html")

    elif path == "/name":
        name = load_name()
        if method == "POST":
            data = parse_post(environ)
            name = data.get("name", [""])[0]
            save_name(name)
        body = render_template("templates/name.html", name=name, name_display=name or "未設定")

    elif path == "/greeting":
        greeting = get_greeting()
        body = render_template("templates/greeting.html", greeting=greeting, name_display=name or "ゲスト")

    else:
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return [b"Not Found"]

    start_response("200 OK", headers)
    return [body.encode("utf-8")]


if __name__ == "__main__":
    port = 8000
    with make_server("", port, application) as httpd:
        print(f"http://localhost:{port} でアクセスしてください")
        httpd.serve_forever()
