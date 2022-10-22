import sqlite3

connection = sqlite3.connect('qr_project.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users ( 
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  email TEXT NOT NULL,
                  password TEXT NOT NULL)""")

connection.commit()


def register_user(username, email, password):
    cursor.execute("""INSERT INTO users(username, email, password)
                        VALUES (?, ?, ?)""", (username, email, password))
    connection.commit()