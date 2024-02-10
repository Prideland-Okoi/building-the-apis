from flask import Flask, render_template
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from models import Member, Contribution, Expenses, engine

app = Flask(__name__)

Session = sessionmaker(bind=engine)
session = Session()

def calculate_total_contribution(member):
    return sum([contribution.amount for contribution in member.contributions])

def calculate_total_goods_expenses():
    return session.query(func.sum(Expenses.cost)).scalar() or 0

# Monthly contribution per member
monthly_contribution = 6000

# Fetch all members from the database
members = session.query(Member).all()

# Calculate total contribution
total_contribution = sum(calculate_total_contribution(member) for member in members)

# Calculate total goods and expenses
total_goods_expenses = calculate_total_goods_expenses()

# Calculate balance
balance = total_contribution - total_goods_expenses


@app.route('/')
def summary():
    # Adjust this according to your needs, as contributions and goods_expenses are not defined in your code
    return render_template('summary.html', total_contribution=total_contribution, total_goods_expenses=total_goods_expenses, balance=balance)

@app.route('/individual/<member_name>')
def individual(member_name):
    member = session.query(Member).filter_by(full_name=member_name).first()
    if member:
        return render_template('individual.html', full_name=member.full_name,
                               department=member.department, company=member.company,
                               contributions=member.contributions,
                               total_contribution=member.total_contribution)
    else:
        return "Member not found"

if __name__ == '__main__':
    app.run(debug=True)
