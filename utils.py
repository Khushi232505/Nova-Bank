import json


def save_data(customers):
    with open("accounts.json", "w") as file:
        json.dump(customers, file, indent=4)


def load_data():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
    
def generate_account_number(customers):

    if len(customers) == 0:
        return "ACC1001"

    last_account = customers[-1]["account_number"]

    number = int(last_account[3:])

    return f"ACC{number + 1}"

def validate_name():

    while True:

        name = input("Enter Account Holder Name: ").strip()

        if name == "":
            print("❌ Name cannot be empty!")
            continue

        if not all(part.isalpha() for part in name.split()):
            print("❌ Name should contain only alphabets!")
            continue

        return name


def validate_age():

    while True:

        try:
            age = int(input("Enter Age: "))

            if age < 18 or age > 120:
                print("❌ Age must be between 18 and 120.")
                continue

            return age

        except ValueError:
            print("❌ Invalid Age! Please enter numbers only.")


def validate_mobile():

    while True:

        mobile = input("Enter Mobile Number: ").strip()

        if not mobile.isdigit():
            print("❌ Mobile number should contain only digits.")
            continue

        if len(mobile) != 10:
            print("❌ Mobile number must be exactly 10 digits.")
            continue

        return mobile
    

def validate_balance(): 

    while True:

        try:
            balance = float(input("Enter Opening Balance: "))

            if balance < 0:
                print("❌ Balance cannot be negative.")
                continue

            return balance

        except ValueError:
            print("❌ Invalid Balance! Please enter a valid number.")


def validate_email():

    while True:

        email = input("Enter Email (Optional): ").strip()

        # Allow empty email
        if email == "":
            return email

        if "@" not in email or "." not in email:
            print("❌ Invalid Email Address.")
            continue

        return email