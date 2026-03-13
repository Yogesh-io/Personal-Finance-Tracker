from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database Configuration
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'finance.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Transaction Model
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    type = db.Column(db.String(10), nullable=False) # 'income' or 'expense'

    def __repr__(self):
        return f'<Transaction {self.description}>'

# Create Database
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    transactions = Transaction.query.order_by(Transaction.date.desc()).all()
    
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type == 'income').scalar() or 0.0
    total_expense = db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type == 'expense').scalar() or 0.0
    balance = total_income - total_expense
    
    return render_template('index.html', transactions=transactions, balance=balance, income=total_income, expense=total_expense)

@app.route('/add', methods=['POST'])
def add_transaction():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    category = request.form.get('category')
    date_str = request.form.get('date')
    t_type = request.form.get('type')

    date = datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else datetime.utcnow().date()

    new_transaction = Transaction(
        description=description,
        amount=amount,
        category=category,
        date=date,
        type=t_type
    )

    db.session.add(new_transaction)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_transaction(id):
    transaction = Transaction.query.get_or_404(id)
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
