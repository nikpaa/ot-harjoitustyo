import sqlite3

db = sqlite3.connect("history.db")
db.isolation_level = None

def create_table():
    db.execute("CREATE TABLE IF NOT EXISTS History (id INTEGER PRIMARY KEY, Operation TEXT, Result FLOAT);")


def add_operation_to_db(operation, result):
    db.execute("INSERT INTO History (Operation, Result) VALUES (?, ?)", [operation, result])

def delete_operation_from_db():
    db.execute("DELETE FROM History WHERE id = (SELECT MAX(id) FROM History)")

def print_history():
    data = db.execute("SELECT Operation, Result FROM History").fetchall()

    print(data)

def clear_table():
    db.execute("DELETE FROM History")
