# ライブラリから使いたい関数・クラスをimport
from flask import Flask, render_template

# Flaskアプリケーションの作成
app = Flask(__name__)

# http://URL/ にGETリクエストが送信されるときに、この関数が処理される
@app.get("/")
def index():
	return "Hello world"

# もしターミナルから直接呼ばれたなら
if __name__ == '__main__':
	# サーバーを立ち上げる
	app.run(debug=True)
