from app_logic import set_new_time, get_my_greeting
from utils import render_template


def greet_with_time():
    set_new_time()
    greeting = get_my_greeting()

    return render_template("boundaries/greeting.html", greeting=greeting)