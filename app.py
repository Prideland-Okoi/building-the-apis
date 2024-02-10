from flask import Flask, render_template, flash
from flask import redirect, url_for, request, current_app
from flask_bootstrap import Bootstrap
from sqlalchemy import func
from models import db, Member, Contribution, Expenses
from forms import MemberForm, ContributionForm, ExpenseForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "hdaduduya55225nn"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coop_app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


# Create instances of Flask extensions
db.init_app(app)
with app.app_context():
    db.create_all()
bootstrap = Bootstrap(app)


@app.context_processor
def inject_data():
    try:
        total_contribution = (
            db.session.query(func.sum(Contribution.amount)).scalar() or 0
        )
        total_expenses = (
            db.session.query(func.sum(Expenses.cost)).scalar() or 0
        )
        wallet = total_contribution - total_expenses
    except Exception as e:
        current_app.logger.error(
            f"Error retrieving data for context processor: {e}"
        )
        wallet = 0

    return {"wallet": wallet}


@app.route("/")
def summary():
    members = Member.query.all()

    # Calculate total contribution for each member
    member_contributions = {}
    for member in members:
        total_contribution = sum(
            contribution.amount for contribution in member.contributions
        )
        member_contributions[member.id] = total_contribution

    expenses = Expenses.query.all()
    total_expenses = sum(expense.cost for expense in expenses)
    contributions = Contribution.query.all()
    total_contribution = sum(
        contribution.amount for contribution in contributions
    )
    return render_template(
        "summary.html",
        members=members,
        expenses=expenses,
        member_contributions=member_contributions,
        total_expenses=total_expenses,
        total_contribution=total_contribution,
    )


@app.route("/contribution_details/<member_id>", methods=["GET"])
def contribution_details(member_id):
    member = Member.query.get_or_404(member_id)
    if member:
        contributions = member.contributions
        total_contribution = sum(
            contribution.amount for contribution in contributions
        )
        return render_template(
            "individual.html",
            title="Individual Details",
            member=member,
            contributions=contributions,
            total_contribution=total_contribution,
        )
    else:
        # Handle case where member with provided ID is not found
        return "Member not found", 404


@app.route("/create_member", methods=["GET", "POST"])
def create_member():
    form = MemberForm()
    if form.validate_on_submit():
        full_name = form.full_name.data
        department = form.department.data
        company = form.company.data

        # Check if a member with the same full_name already exists
        existing_member = Member.query.filter_by(full_name=full_name).first()
        if existing_member:
            flash("A member with the same name already exists.", "danger")
        else:
            new_member = Member(
                full_name=full_name, department=department, company=company
            )
            try:
                db.session.add(new_member)
                db.session.commit()
                flash("Member added successfully!", "success")
                return redirect(url_for("summary"))
            except Exception as e:
                flash(
                    "An error occurred while adding the member.",
                    "danger",
                )
                db.session.rollback()
                current_app.logger.error(f"Error adding expense: {e}")

    return render_template("create_member.html", form=form)


@app.route("/create_expense", methods=["GET", "POST"])
def create_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        item = form.item.data
        cost = form.cost.data

        new_expense = Expenses(item=item, cost=cost)

        try:
            db.session.add(new_expense)
            db.session.commit()
            flash("Expense added successfully!", "success")
            return redirect(url_for("summary"))
        except Exception as e:
            flash(
                "An error occurred while adding the expense.",
                "danger",
            )
            db.session.rollback()
            current_app.logger.error(f"Error adding expense: {e}")

    return render_template("create_expense.html", form=form)


@app.route("/create_contribution", methods=["GET", "POST"])
def create_contribution():
    form = ContributionForm()
    form.member_id.choices = [
        (member.id, member.full_name) for member in Member.query.all()
    ]

    if form.validate_on_submit():
        month = form.month.data
        amount = form.amount.data
        member_id = form.member_id.data

        new_contribution = Contribution(
            month=month, amount=amount, member_id=member_id
        )

        try:
            db.session.add(new_contribution)
            db.session.commit()
            flash("Contribution added successfully!", "success")
            return redirect(url_for("summary"))
        except Exception as e:
            flash(
                "An error occurred while adding the contribution.",
                "danger",
            )
            db.session.rollback()
            current_app.logger.error(f"Error adding expense: {e}")

    return render_template("create_contribution.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
