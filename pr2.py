import sqlite3

connection = sqlite3.connect("Student.db")
print(connection.total_changes)
