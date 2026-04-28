import sqlite3

def get_connection():
    conn = sqlite3.connect("transactions.db")
    conn.row_factory = sqlite3.Row
    return conn


def execute_query(sql, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        result = cursor.fetchall()
        return [dict(row) for row in result]
    finally:
        conn.close()


def save_query_history(user_id, question, sql, result, insight):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO query_history (user_id, question, sql_query, result, insight)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, question, sql, str(result), insight))

    conn.commit()
    conn.close()


def get_query_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM query_history
    WHERE user_id = ?
    ORDER BY created_at DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_total_spending(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUM(amount) as total
    FROM transactions
    WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    conn.close()

    return result["total"] if result["total"] else 0


def get_spending_by_category(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount) as total
    FROM transactions
    WHERE user_id = ?
    GROUP BY category
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def get_top_category(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount) as total
    FROM transactions
    WHERE user_id = ?
    GROUP BY category
    ORDER BY total DESC
    LIMIT 1
    """, (user_id,))

    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None