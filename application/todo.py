from model.todo import Todo

# todoの作成
def create_todo(db, todo):
	# DBを操作するためにカーソルを取得
	cur = db.cursor()
	# クエリの実行
	cur.execute("INSERT INTO todo(content) VALUES (?)", (todo.content,))
	# 変更の反映
	db.commit()
	cur.close()

# Todoクラスのリストを返す
def get_todo_list(db):
	cur = db.cursor()
	res = cur.execute("SELECT id, content FROM todo")
	todo_list = []
	# fetchallで結果を取得する
	for row in res.fetchall():
		# 取得した結果をTodoクラスに直す
		todo_list.append(Todo(id=row[0], content=row[1]))
	cur.close()
	return todo_list

# todoの削除
def delete_todo(db, todo_id):
	cur = db.cursor()
	cur.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
	db.commit()
	cur.close()
