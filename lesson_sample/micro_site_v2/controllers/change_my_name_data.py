from app_logic import set_my_name, get_my_name
from utils import parse_post, render_template


def change_my_name_data(environ):
    name = get_my_name()
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        name = data.get("name", [""])[0]
        set_my_name(name)

    return render_template("boundaries/name.html", name=name, name_display=name or "未設定")