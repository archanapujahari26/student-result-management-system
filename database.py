import sqlite3

def connect():
    return sqlite3.connect("student.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        subject1 INTEGER,
        subject2 INTEGER,
        subject3 INTEGER,
        percentage REAL,
        grade TEXT
    )
    """)
    
    conn.commit()
    conn.close()
