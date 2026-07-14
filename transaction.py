from database import customers
from utils import save_data
from datetime import datetime

# Deposit Money
def deposit_money():
    print("\n========== DEPOSIT MONEY ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            amount = float(input("Enter Deposit Amount: "))

            if amount <= 0:
                print("❌ Invalid Amount!")
                return

            customer["balance"] += amount
            if "transactions" not in customer:
                customer["transactions"] = []
        
            transaction = {
    "type": "Deposit",
    "amount": amount,
    "date": datetime.now().strftime("%d-%m-%Y"),
    "time": datetime.now().strftime("%I:%M %p"),
    "balance_after": customer["balance"]
}
            customer["transactions"].append(transaction)
            save_data(customers)

            print("\n✅ Money Deposited Successfully!")
            print(f"Updated Balance : ₹{customer['balance']}")
            return

    print("❌ Account Not Found!")


# Withdraw Money
def withdraw_money():
    print("\n========== WITHDRAW MONEY ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= 0:
                print("❌ Invalid Amount!")
                return

            if customer["balance"] >= amount:

                customer["balance"] -= amount
                if "transactions" not in customer:
                    customer["transactions"] = []
                transaction = {
    "type": "Withdraw",
    "amount": amount,
    "date": datetime.now().strftime("%d-%m-%Y"),
    "time": datetime.now().strftime("%I:%M %p"),
    "balance_after": customer["balance"]
}

            customer["transactions"].append(transaction)
            save_data(customers)
            print("\n✅ Money Withdrawn Successfully!")
            print(f"Remaining Balance : ₹{customer['balance']}")

        else:
                print("❌ Insufficient Balance!")

        return

    print("❌ Account Not Found!")


# Check Balance
def check_balance():
    print("\n========== CHECK BALANCE ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            print("\nAccount Found")
            print(f"Account Holder : {customer['name']}")
            print(f"Current Balance : ₹{customer['balance']}")
            return

    print("❌ Account Not Found!")



def view_transaction_history():

    print("\n========== TRANSACTION HISTORY ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            if "transactions" not in customer or len(customer["transactions"]) == 0:

                print("No Transactions Found!")
                return

            for transaction in customer["transactions"]:

                print("\n----------------------------")
                print(f"Type : {transaction['type']}")
                print(f"Amount : ₹{transaction['amount']}")
                print(f"Date : {transaction['date']}")
                print(f"Time : {transaction['time']}")
                print(f"Balance After : ₹{transaction['balance_after']}")

            return

    print("❌ Account Not Found!")


from datetime import datetime

def transfer_money():

    print("\n========== TRANSFER MONEY ==========")

    sender_acc = input("Enter Sender Account Number: ")
    receiver_acc = input("Enter Receiver Account Number: ")

    if sender_acc == receiver_acc:
        print("❌ Sender and Receiver cannot be the same.")
        return

    sender = None
    receiver = None

    for customer in customers:
        if customer["account_number"] == sender_acc:
            sender = customer

        if customer["account_number"] == receiver_acc:
            receiver = customer

    if sender is None:
        print("❌ Sender Account Not Found!")
        return

    if receiver is None:
        print("❌ Receiver Account Not Found!")
        return

    amount = float(input("Enter Transfer Amount: "))

    if amount <= 0:
        print("❌ Invalid Amount!")
        return

    if sender["balance"] < amount:
        print("❌ Insufficient Balance!")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    if "transactions" not in sender:
        sender["transactions"] = []

    if "transactions" not in receiver:
        receiver["transactions"] = []

    sender["transactions"].append({
        "type": "Transfer Sent",
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "balance_after": sender["balance"]
    })

    receiver["transactions"].append({
        "type": "Transfer Received",
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "balance_after": receiver["balance"]
    })

    save_data(customers)

    print("\n✅ Money Transferred Successfully!")

def deposit_money_web(account_number, amount):

    amount = float(amount)

    for customer in customers:

        if customer["account_number"] == account_number:

            if amount <= 0:
                return False, "Invalid Amount!"

            customer["balance"] += amount

            if "transactions" not in customer:
                customer["transactions"] = []

            transaction = {
                "type": "Deposit",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y"),
                "time": datetime.now().strftime("%I:%M %p"),
                "balance_after": customer["balance"]
            }

            customer["transactions"].append(transaction)

            save_data(customers)

            return True, customer["balance"]

    return False, "Account Not Found!"


def withdraw_money_web(account_number, amount):

    amount = float(amount)

    for customer in customers:

        if customer["account_number"] == account_number:

            if amount <= 0:
                return False, "Invalid Amount!"

            if customer["balance"] < amount:
                return False, "Insufficient Balance!"

            customer["balance"] -= amount

            if "transactions" not in customer:
                customer["transactions"] = []

            transaction = {
                "type": "Withdraw",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y"),
                "time": datetime.now().strftime("%I:%M %p"),
                "balance_after": customer["balance"]
            }

            customer["transactions"].append(transaction)

            save_data(customers)

            return True, customer["balance"]

    return False, "Account Not Found!"


def view_transaction_history_web(account_number):

    for customer in customers:

        if customer["account_number"] == account_number:

            if "transactions" not in customer or len(customer["transactions"]) == 0:
                return False, "No Transactions Found!"

            return True, customer["transactions"]

    return False, "Account Not Found!"

def transfer_money_web(sender_acc, receiver_acc, amount):

    amount = float(amount)

    if sender_acc == receiver_acc:
        return False, "Sender and Receiver cannot be the same!"

    sender = None
    receiver = None

    for customer in customers:
        if customer["account_number"] == sender_acc:
            sender = customer

        if customer["account_number"] == receiver_acc:
            receiver = customer

    if sender is None:
        return False, "Sender Account Not Found!"

    if receiver is None:
        return False, "Receiver Account Not Found!"

    if amount <= 0:
        return False, "Invalid Amount!"

    if sender["balance"] < amount:
        return False, "Insufficient Balance!"

    sender["balance"] -= amount
    receiver["balance"] += amount

    if "transactions" not in sender:
        sender["transactions"] = []

    if "transactions" not in receiver:
        receiver["transactions"] = []

    from datetime import datetime

    sender["transactions"].append({
        "type": "Transfer Sent",
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "balance_after": sender["balance"]
    })

    receiver["transactions"].append({
        "type": "Transfer Received",
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "balance_after": receiver["balance"]
    })

    save_data(customers)

    return True, "Transfer Successful!"
