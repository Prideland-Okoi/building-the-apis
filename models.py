# models.py

class Member:
    def __init__(self, full_name, department, company, contributions):
        self.full_name = full_name
        self.department = department
        self.company = company
        self.contributions = contributions
        self.total_contribution = sum(contributions.values())

class Contribution:
    def __init__(self, month, amount):
        self.month = month
        self.amount = amount

class Expenses:
    def __init__(self, item, cost):
        self.item = item
        self.cost = cost

