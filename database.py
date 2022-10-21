import sqlite3

connection = sqlite3.connect('qr_project.db', check_same_thread=False)
cursor = connection.cursor()