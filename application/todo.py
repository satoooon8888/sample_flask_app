from uuid import uuid4

def create_todo(db, todo):
	cur = db.cursor()
	cur.execute("INSERT INTO todo(content) VALUES (?)", (todo,))
	db.commit()
	cur.close()


def get_todo_list(db):
	cur = db.cursor()
	res = cur.execute("SELECT content FROM todo");
	todo_list = []
	for row in res.fetchall():
		todo_list.append(row[0])
	cur.close()
	return todo_list

