"""
Forms module for defining Flask-WTF forms.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Member


class UniqueName:
    """
    Validator to ensure unique full name.
    """
    def __init__(self, message='This name already exists.'):
        self.message = message

    def __call__(self, form, field):
        existing_name = Member.query.filter_by(full_name=field.data).first()
        if existing_name:
            raise ValidationError(self.message)


class MemberForm(FlaskForm):
    """
    Form for adding a new member.
    """
    full_name = StringField(
        'Full Name', validators=[DataRequired(), Length(max=60), UniqueName()]
        )
    department = StringField('Department', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Add Member')


class ContributionForm(FlaskForm):
    """
    Form for adding a contribution.
    """
    month = StringField('Month', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    member_id = SelectField('Member', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Contribution')


class ExpenseForm(FlaskForm):
    """
    Form for adding an expense.
    """
    item = StringField('Item', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    submit = SubmitField('Add Expense')
