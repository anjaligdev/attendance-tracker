import sqlite3
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    school TEXT NOT NULL,
    batch TEXT NOT NULL
)
""")
conn.commit()
conn.close()
print("Database and students table created successfully.")