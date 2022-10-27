from model.todo import Todo

def create_todo(db, todo):
	cur = db.cursor()
	cur.execute("INSERT INTO todo(content) VALUES (?)", (todo.content,))
	db.commit()
	cur.close()


def get_todo_list(db):
	cur = db.cursor()
	res = cur.execute("SELECT id, content FROM todo")
	todo_list = []
	for row in res.fetchall():
		todo_list.append(Todo(id=row[0], content=row[1]))
	cur.close()
	return todo_list

