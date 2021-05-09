import sqlite3

db = sqlite3.connect("history.db")
db.isolation_level = None

def create_table():
    """Funcion that creates the database for storing the history
    """
    db.execute("CREATE TABLE IF NOT EXISTS History (id INTEGER PRIMARY KEY, Operation TEXT, Result FLOAT);")

def add_operation_to_db(operation, result):
    """Add operation and its result to history
    """
    db.execute("INSERT INTO History (Operation, Result) VALUES (?, ?)", [operation, result])

def delete_operation_from_db():
    """Deletes the latest operation from the history
    """
    db.execute("DELETE FROM History WHERE id = (SELECT MAX(id) FROM History)")

def print_history():
    """Prints the operation history
    """
    data = db.execute("SELECT Operation, Result FROM History").fetchall()

    for row in data:
        print(f"{row[0]} = {row[1]}")

def clear_table():
    """Clears the operation history
    """
    db.execute("DELETE FROM History")
