import sqlite3
op = sqlite3.connect("zone-h.db")
cs = op.cursor()

cs.execute("CREATE TABLE teams(id integer primary key AUTOINCREMENT,teamname TEXT,teamurl TEXT)")
op.commit()
op.close()