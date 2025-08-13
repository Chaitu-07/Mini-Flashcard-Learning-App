import sqlite3

c.execute('''
CREATE TABLE IF NOT EXISTS flashcards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category TEXT
)
''')

sample_flashcards = [
    ("What is Python?", "Python is a high-level programming language.", "Python"),
    ("What is Flask?", "Flask is a micro web framework for Python.", "Python"),
    ("What is SQL?", "SQL is a language to manage databases.", "SQL"),
    ("What does HTML stand for?", "HyperText Markup Language", "Web Development"),
    ("What is CSS used for?", "CSS is used for styling HTML elements.", "Web Development"),
    ("What is a database?", "A database stores structured data.", "SQL"),
    ("What is a primary key?", "A unique identifier for a database table row.", "SQL"),
    ("What is a function in Python?", "A block of reusable code that performs a task.", "Python"),
    ("What is JavaScript?", "A scripting language for interactive web pages.", "Web Development"),
    ("What is Git?", "A version control system to track code changes.", "Tools")
]

c.execute('SELECT COUNT(*) FROM flashcards')
count = c.fetchone()[0]

if count == 0:
    c.executemany('INSERT INTO flashcards (question, answer, category) VALUES (?, ?, ?)', sample_flashcards)
    print("Sample flashcards added!")

conn.commit()
conn.close()
print("Database initialized!")
