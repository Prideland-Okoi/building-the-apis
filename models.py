# models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    department = Column(String)
    company = Column(String)
    total_contribution = Column(Float)

    contributions = relationship("Contribution", back_populates="member")

    def __init__(self, full_name, department, company, contributions):
        self.full_name = full_name
        self.department = department
        self.company = company
        self.contributions = contributions
        self.total_contribution = sum(contributions.values())

class Contribution(Base):
    __tablename__ = 'contributions'

    id = Column(Integer, primary_key=True)
    month = Column(String)
    amount = Column(Float)
    member_id = Column(Integer, ForeignKey('members.id'))

    member = relationship("Member", back_populates="contributions")

    def __init__(self, month, amount):
        self.month = month
        self.amount = amount

class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    item = Column(String)
    cost = Column(Float)

    def __init__(self, item, cost):
        self.item = item
        self.cost = cost
