import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "expenses.db"

def generate_monthly_summary():
    """Generate a monthly summary report."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    
    monthly_summary = df.groupby('month')['amount'].sum()
    print("\nMonthly Expense Summary:")
    print(monthly_summary)
    
    monthly_summary.plot(kind='bar', title="Monthly Expenses")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.show()

def generate_category_summary():
    """Generate category-wise expenditure analysis."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    
    category_summary = df.groupby('category')['amount'].sum()
    print("\nCategory-wise Expense Summary:")
    print(category_summary)
    
    category_summary.plot(kind='pie', title="Expense by Category", autopct='%1.1f%%')
    plt.ylabel("")  # Hide y-label
    plt.show()
