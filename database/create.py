import sqlite3

from database.session import session
from database.query import Query


create_notes_table = '''
CREATE TABLE IF NOT EXISTS notes (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title VARCHAR,
		content VARCHAR
	);
'''


def rollout():
    with session() as s:
        s.execute(Query(create_notes_table))
