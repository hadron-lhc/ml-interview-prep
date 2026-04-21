import sqlite3
from pathlib import Path

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

with open("schema.sql", "r") as f:
    cur.executescript(f.read())

with open("exercises.sql", "r") as f:
    query = f.read()

rows = cur.execute(query).fetchall()

for row in rows:
    print(row)

conn.close()
