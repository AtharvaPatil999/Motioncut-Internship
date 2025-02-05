import sqlite3

DB_NAME = "expenses.db"

def init_db():
    """Initialize the database and create table if not exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses 
                      (id INTEGER PRIMARY KEY, date TEXT, amount REAL, category TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def add_expense(date, amount, category, description):
    """Adds a new expense entry to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, amount, category, description) VALUES (?, ?, ?, ?)",
                   (date, amount, category, description))
    conn.commit()
    conn.close()

def fetch_expenses():
    """Fetch all expenses."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()
    conn.close()
    return data

def get_category_wise_summary():
    """Get total expenditure per category."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return data
