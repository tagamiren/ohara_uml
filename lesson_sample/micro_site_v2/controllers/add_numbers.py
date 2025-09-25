from utils import render_template
from app_logic import set_first_value, set_second_value



def add_numbers(environ):
    # ここに処理を書く
    set_first_value("10")
    set_second_value("5")
    # get_addition()

    # additionの結果を渡す
    return render_template("boundaries/add_numbers_data.html")