import sqlite3

def init_db():
    connection = sqlite3.connect('finance_tracker.db')  # Use relative path
    cursor = connection.cursor()

    # Create transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        type TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()
