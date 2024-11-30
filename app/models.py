from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
#from app import db

from app import db

from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'category': self.category,
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d')  # Convert date to string for JSON compatibility
        }


def get_transactions():
    # Connect to the database
    connection = sqlite3.connect('finance_tracker.db')
    cursor = connection.cursor()

    # Fetch transactions from the database
    cursor.execute('SELECT id, date, type, category, amount FROM transactions')
    rows = cursor.fetchall()

    # Convert rows to Transaction objects
    transactions = [Transaction(*row) for row in rows]

    connection.close()
    return transactions
