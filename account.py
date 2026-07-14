from database import customers
from utils import save_data, generate_account_number, validate_name, validate_age, validate_mobile, validate_balance, validate_email

def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    name = validate_name()
    age = validate_age()
    gender = input("Enter Gender: ")
    mobile = validate_mobile()
    address = input("Enter Address: ")
    email = validate_email()
    balance = validate_balance()

    account_number = generate_account_number(customers)

    customer = {
        "account_number": account_number,
        "name": name,
        "age": age,
        "gender": gender,
        "mobile": mobile,
        "address": address,
        "email": email,
        "balance": balance,
        "transactions": []
    }

    customers.append(customer)
    save_data(customers)

    print("\n🎉 Account Created Successfully!")
    print(f"Account Number : {account_number}")
    print(f"Account Holder : {name}")
    print(f"Current Balance : ₹{balance}")

 
    print("\nCustomer Data:")



def search_account():

    print("\n========== SEARCH ACCOUNT ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            print("\nAccount Found")
            print(f"Account Number : {customer['account_number']}")
            print(f"Name : {customer['name']}")
            print(f"Age : {customer['age']}")
            print(f"Gender : {customer['gender']}")
            print(f"Mobile : {customer['mobile']}")
            print(f"Address : {customer['address']}")
            print(f"Email : {customer['email']}")
            print(f"Balance : ₹{customer['balance']}")

            return

    print("❌ Account Not Found!")
    



def update_account():

    print("\n========== UPDATE ACCOUNT ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            customer["name"] = input("Enter New Name: ")
            customer["mobile"] = input("Enter New Mobile: ")
            customer["address"] = input("Enter New Address: ")
            customer["email"] = input("Enter New Email: ")

            print("\n✅ Account Updated Successfully!")

            return

    print("❌ Account Not Found!")



def delete_account():

    print("\n========== DELETE ACCOUNT ==========")

    account_number = input("Enter Account Number: ")

    for customer in customers:

        if customer["account_number"] == account_number:

            customers.remove(customer)
            save_data(customers)

            print("\n✅ Account Deleted Successfully!")

            return

    print("❌ Account Not Found!")




def display_all_accounts():

    print("\n========== ALL ACCOUNTS ==========")

    if len(customers) == 0:
        print("No Accounts Available")
        return

    for customer in customers:

        print("------------------------------")
        print(f"Account Number : {customer['account_number']}")
        print(f"Name : {customer['name']}")
        print(f"Balance : ₹{customer['balance']}")


def create_account_web(name, age, gender, mobile, address, email, balance):

    account_number = generate_account_number(customers)

    customer = {
        "account_number": account_number,
        "name": name,
        "age": int(age),
        "gender": gender,
        "mobile": mobile,
        "address": address,
        "email": email,
        "balance": float(balance),
        "transactions": []
    }

    customers.append(customer)
    save_data(customers)

    return account_number

def update_account_web(account_number, mobile, address, email):

    for customer in customers:

        if customer["account_number"] == account_number:

            customer["mobile"] = mobile
            customer["address"] = address
            customer["email"] = email

            save_data(customers)

            return True, "Updated"

    return False, "Account Not Found!"

def update_account_web(account_number, mobile, address, email):

    for customer in customers:

        if customer["account_number"] == account_number:

            customer["mobile"] = mobile
            customer["address"] = address
            customer["email"] = email

            save_data(customers)

            return True, "Updated Successfully!"

    return False, "Account Not Found!"

def delete_account_web(account_number):

    for customer in customers:

        if customer["account_number"] == account_number:

            customers.remove(customer)

            save_data(customers)

            return True, "Deleted Successfully!"

    return False, "Account Not Found!"