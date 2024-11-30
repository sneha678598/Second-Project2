from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from . import db
from .models import Transaction  # Import the model correctly
from .models import get_transactions
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

main = Blueprint('main', __name__)

@main.route('/')
def index():
    
    # transactions = get_transactions()  # Fetch your transactions here
    # transactions_dict = [transaction.to_dict() for transaction in transactions]
    # return render_template('index.html', transactions=transactions_dict)

    transactions = Transaction.query.all()  # Fetch all transactions
    transactions_dict = [transaction.to_dict() for transaction in transactions]  # Convert to dict if needed
    return render_template('index.html', transactions=transactions_dict)



@main.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        type = request.form.get('type')
        category = request.form.get('category')
        amount = float(request.form.get('amount'))
        date_str = request.form.get('date')  # Date string from the form

        # Convert string to date object
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD.", 400

        # Create and add new transaction
        new_transaction = Transaction(type=type, category=category, amount=amount, date=date)
        db.session.add(new_transaction)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('add_transaction.html')


@main.route('/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)  # Correct: Use 'transaction_id'
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
    return redirect(url_for('main.index'))


