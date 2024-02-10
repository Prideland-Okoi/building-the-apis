"""
Module for defining database models.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    """
    Model class for members.
    """
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(60), unique=True, nullable=False)
    department = db.Column(db.String)
    company = db.Column(db.String)

    contributions = db.relationship("Contribution", back_populates="member")

    def __init__(self, full_name, department, company):
        self.full_name = full_name
        self.department = department
        self.company = company


class Contribution(db.Model):
    """
    Model class for contributions.
    """
    __tablename__ = 'contributions'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String)
    amount = db.Column(db.Float)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))

    member = db.relationship("Member", back_populates="contributions")

    def __init__(self, member_id, month, amount):
        self.member_id = member_id
        self.month = month
        self.amount = amount


class Expenses(db.Model):
    """
    Model class for expenses.
    """
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String)
    cost = db.Column(db.Float)

    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
