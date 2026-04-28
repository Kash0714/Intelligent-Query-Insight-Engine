import sqlite3

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    category TEXT,
    merchant TEXT,
    transaction_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS query_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    question TEXT,
    sql_query TEXT,
    result TEXT,
    insight TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

data = [
    (1, 500, "food", "Zomato", "2026-03-10"),
    (1, 1200, "shopping", "Amazon", "2026-03-12"),
    (1, 300, "food", "Swiggy", "2026-03-15"),
    (1, 2000, "travel", "Uber", "2026-03-18")
]

cursor.executemany("""
INSERT INTO transactions (user_id, amount, category, merchant, transaction_date)
VALUES (?, ?, ?, ?, ?)
""", data)

conn.commit()
conn.close()