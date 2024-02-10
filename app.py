from flask import Flask, render_template
from models import Member, Contribution, Expenses

app = Flask(__name__)

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
    return render_template('summary.html', contributions=contributions, goods_expenses=goods_expenses, total_contribution=total_contribution, total_goods_expenses=total_goods_expenses, balance=balance)

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
