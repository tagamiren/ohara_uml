# controllers/add_number.py

from utils import render_template
from urllib.parse import parse_qs

def add_number(environ):
    method = environ["REQUEST_METHOD"]

    if method == "GET":
        # GETリクエストの場合はフォームを表示
        return render_template("boundaries/add_num_bers_data.html")

    elif method == "POST":
        # POSTリクエストの場合はフォームデータを処理
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
            form_data = parse_qs(request_body)

            # フォームから数字を取得
            num1 = int(form_data.get('num1', ['0'])[0])
            num2 = int(form_data.get('num2', ['0'])[0])
            result = num1 + num2

            # 結果をテンプレートに渡して表示
            return render_template("boundaries/calcresult.html", result=result)
        except (ValueError, KeyError):
            # 無効な入力があった場合はエラーメッセージを返す
            return "無効な入力です。"