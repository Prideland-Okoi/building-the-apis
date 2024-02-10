from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from models import Member


class UniqueName(object):
    def __init__(self, message='This name already exists.'):
        self.message = message

    def __call__(self, form, field):
        existing_name = Member.query.filter_by(full_name=field.data).first()
        if existing_name:
            raise ValidationError(self.message)


class MemberForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=60), UniqueName()])
    department = StringField('Department', validators=[DataRequired()])
    company = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Add Member')


class ContributionForm(FlaskForm):
    month = StringField('Month', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
    member_id = SelectField('Member', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Contribution')


class ExpenseForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    submit = SubmitField('Add Expense')
