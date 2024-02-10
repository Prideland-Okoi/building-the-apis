from flask import Flask, render_template

app = Flask(__name__)

members_data = {
    "Mr Albert": {
        "full_name": "Mr Albert Odama",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mrs Jacinta": {
        "full_name": "Mrs Jacinta Ogbonna",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Omini": {
        "full_name": "Mr Omini Okoi",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mrs Henrietta": {
        "full_name": "Mrs Henrietta Elijuoke",
        "department": "Administration",
        "company": "Atlantic Shrimpers Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },

    "Mr Micah": {
        "full_name": "Mr Micah Ogbuka",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Fortunate": {
        "full_name": "Mr Fortunate Ewelike",
        "department": "Production",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Junior": {
        "full_name": "Mr Junior Akudiwe",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Emmanuel": {
        "full_name": "Mr Emnanuel Inyokwe",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
        
    "Mr Anthony": {
        "full_name": "Mr Emmanuel Anthony",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Musiliu": {
        "full_name": "Mr Musiliu Odewale",
        "department": "Health, Safety and Environment",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },

    "Mr Donatus": {
        "full_name": "Mr Donatus Odunze",
        "department": "Security",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    "Mr Ikenna": {
        "full_name": "Mr Ikenna Wilson",
        "department": "Quality Control",
        "company": "Royal Salt Limited",
        "contributions": {"May": 6000, "June": 6000, "July": 6000, "August": 6000, "September": 6000, "October": 6000, "November": 6000, "December": 6000},
        "total_contribution": 48000
    },
    
}

# Contribution data
contributions = {
    "Mr Albert": 48000,
    "Mrs Jacinta": 48000,
    "Mr Omini": 48000,
    "Mrs Henrietta": 48000,
    "Mr Micah": 48000,
    "Mr Fortunate": 48000,
    "Mr Junior": 48000,
    "Mr Emmanuel": 48000,
    "Mr Anthony": 48000,
    "Mr Musiliu": 48000,
    "Mr Donatus": 48000,
    "Mr Ikenna": 48000
}

# Goods and expenses data
goods_expenses = {
    "Oil": 85500,
    "Spaghetti": 120000,
    "Tomato": 56400,
    "Semo": 99600,
    "Idomi": 45000,
    "Sugar": 8400,
    "Magi": 12000,
    "Detergent": 10800,
    "Peak milk": 28800,
    "Milo": 21000,
    "Crayfish": 24000,
    "Stock fish": 12000,
    "Expenses": 4200
}

# Monthly contribution per member
monthly_contribution = 6000

# Calculate total contribution
total_contribution = sum(contributions.values())

# Calculate total goods and expenses
total_goods_expenses = sum(goods_expenses.values())

# Calculate balance
balance = total_contribution - total_goods_expenses

@app.route('/')
def summary():
    return render_template('summary.html', contributions=contributions, goods_expenses=goods_expenses, total_contribution=total_contribution, total_goods_expenses=total_goods_expenses, balance=balance)

@app.route('/individual/<member_name>')
def individual(member_name):
    if member_name in members_data:
        member_details = members_data[member_name]
        return render_template('individual.html', full_name=member_details["full_name"],
                               department=member_details["department"], company=member_details["company"],
                               contributions=member_details["contributions"],
                               total_contribution=member_details["total_contribution"])
    else:
        return "Member not found"
if __name__ == '__main__':
    app.run(debug=True)
