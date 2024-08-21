import sqlite3

conn = sqlite3.connect('people.db')
cursor = conn.cursor()

cursor.execute("SELECT name, age FROM users WHERE age > 30")

rows = cursor.fetchall()

for row in rows:
    print(f"Name: {row[0]}, Age: {row[1]}")

conn.close()