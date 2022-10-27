-- 既にあるテーブルを削除
DROP TABLE IF EXISTS todo;

-- テーブルを定義
CREATE TABLE todo (
	-- id: 主キー
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	-- content: Todoの内容
	content TEXT
);

