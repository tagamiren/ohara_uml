from wsgiref.simple_server import make_server
from controllers.robodog_menu import robodog_menu
from controllers.change_my_name_data import change_my_name_data
from controllers.greet_with_time import greet_with_time
from controllers.add_numbers import add_numbers


def application(environ, start_response):
    path = environ.get("PATH_INFO", "/")
    method = environ["REQUEST_METHOD"]
    headers = [("Content-Type", "text/html; charset=utf-8")]

    if path == "/":
        body = robodog_menu()

    elif path == "/name":
        body = change_my_name_data(environ)

    elif path == "/greeting":
        body = greet_with_time()

    elif path == "/calc":
        body = add_numbers(environ)

    else:
        start_response("404 Not Found", headers)
        return [b"Not Found"]

    start_response("200 OK", headers)
    return [body.encode("utf-8")]


if __name__ == "__main__":
    port = 8000
    with make_server("", port, application) as httpd:
        print(f"http://localhost:{port} でアクセスしてください")
        httpd.serve_forever()
