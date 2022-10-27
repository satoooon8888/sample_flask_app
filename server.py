# ライブラリから使いたい関数・クラスをimport
from flask import Flask, render_template, request, abort, redirect, url_for, g
import sqlite3

# /application/からtodoを立ち上げる
from application.todo import create_todo, get_todo_list

# Flaskアプリケーションの作成
app = Flask(__name__)

@app.before_request
def handle_before_request():
	g.database = sqlite3.connect("db/todo.db")

@app.teardown_request
def handle_teardown_request(exception):
	g.database.close()

# http://URL/ にGETリクエストが送信されるときに、この関数が処理される
@app.get("/")
def index():
	todo_list = get_todo_list(g.database)
	return render_template("index.html", todo_list = todo_list)

# http://URL/todo にPOSTリクエストが送信されるときに、この関数が処理される
@app.post("/todo")
def handle_create_todo():
	# フォームから値を取得
	todo = request.form.get("todo", None)
	# 値が存在しなかったらエラー
	if todo is None:
		return abort(400)

	# todoを作成する
	create_todo(g.database, todo)
	# http://URL/ にリダイレクトさせる
	return redirect("/")

# もしターミナルから直接呼ばれたなら
if __name__ == '__main__':
	# サーバーを立ち上げる
	app.run(debug=True)
