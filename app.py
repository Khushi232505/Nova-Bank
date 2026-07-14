from flask import Flask, render_template, request
from account import create_account_web,  update_account_web, delete_account_web
from transaction import deposit_money_web, withdraw_money_web
from transaction import view_transaction_history_web, transfer_money_web
from database import customers


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        customers=customers
    )


@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        mobile = request.form["mobile"]
        address = request.form["address"]
        email = request.form["email"]
        balance = request.form["balance"]

        account_number = create_account_web(
            name,
            age,
            gender,
            mobile,
            address,
            email,
            balance
        )

        return f"""
        <h2>🎉 Account Created Successfully!</h2>
        <h3>Account Number: {account_number}</h3>
        <a href="/">Go Back Home</a>
        """

    return render_template("create.html")

@app.route("/deposit", methods=["GET", "POST"])
def deposit():

    if request.method == "POST":

        account_number = request.form["account_number"]
        amount = request.form["amount"]

        success, result = deposit_money_web(account_number, amount)

        if success:
            return f"""
            <h2>✅ Money Deposited Successfully!</h2>
            <h3>Updated Balance: ₹{result}</h3>
            <a href='/'>🏠 Back Home</a>
            """

        else:
            return f"""
            <h2>❌ {result}</h2>
            <a href='/deposit'>Try Again</a>
            """

    return render_template("deposit.html")


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():

    if request.method == "POST":

        account_number = request.form["account_number"]
        amount = request.form["amount"]

        success, result = withdraw_money_web(account_number, amount)

        if success:
            return f"""
            <h2>✅ Money Withdrawn Successfully!</h2>
            <h3>Remaining Balance: ₹{result}</h3>
            <a href='/'>🏠 Back Home</a>
            """

        else:
            return f"""
            <h2>❌ {result}</h2>
            <a href='/withdraw'>Try Again</a>
            """

    return render_template("withdraw.html")


@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":

        account_number = request.form["account_number"]

        for customer in customers:

            if customer["account_number"] == account_number:

                return render_template(
                    "search.html",
                    customer=customer
                )

        return "<h2>❌ Account Not Found!</h2>"

    return render_template("search.html")


@app.route("/display")
def display():
    return render_template("display.html", customers=customers)

@app.route("/history", methods=["GET", "POST"])
def history():

    if request.method == "POST":

        account_number = request.form["account_number"]

        success, result = view_transaction_history_web(account_number)

        if success:
            return render_template(
                "history.html",
                transactions=result,
                account_number=account_number
            )

        return f"""
        <h2>❌ {result}</h2>
        <a href="/history">Try Again</a>
        """

    return render_template("history.html")


@app.route("/update", methods=["GET", "POST"])
def update():

    if request.method == "POST":

        account_number = request.form["account_number"]
        mobile = request.form["mobile"]
        address = request.form["address"]
        email = request.form["email"]

        success, message = update_account_web(
            account_number,
            mobile,
            address,
            email
        )

        if success:
            return f"""
            <h2>✅ Account Updated Successfully!</h2>
            <a href="/">🏠 Back Home</a>
            """

        return f"""
        <h2>❌ {message}</h2>
        <a href="/update">Try Again</a>
        """

    return render_template("update.html")

@app.route("/delete", methods=["GET", "POST"])
def delete():

    if request.method == "POST":

        account_number = request.form["account_number"]

        success, message = delete_account_web(account_number)

        if success:

            return """
            <h2>🗑️ Account Deleted Successfully!</h2>
            <a href="/">🏠 Back Home</a>
            """

        return f"""
        <h2>❌ {message}</h2>
        <a href="/delete">Try Again</a>
        """

    return render_template("delete.html")

@app.route("/transfer", methods=["GET", "POST"])
def transfer():

    if request.method == "POST":

        sender = request.form["sender"]
        receiver = request.form["receiver"]
        amount = request.form["amount"]

        success, message = transfer_money_web(
            sender,
            receiver,
            amount
        )

        if success:
            return """
            <h2>✅ Money Transferred Successfully!</h2>
            <a href="/">🏠 Back Home</a>
            """

        return f"""
        <h2>❌ {message}</h2>
        <a href="/transfer">Try Again</a>
        """

    return render_template("transfer.html")

if __name__ == "__main__":
    app.run(debug=True)

