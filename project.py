import json
import random
import string
from pathlib import Path

class Bank:
    database = "data.json"
    data = []

    # Load data
    if Path(database).exists():
        with open(database, "r") as f:
            data = json.load(f)

    @classmethod
    def save(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def generate_account():
        chars = (
            random.choices(string.ascii_letters, k=3) +
            random.choices(string.digits, k=3) +
            random.choices("!@#$%", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    @classmethod
    def find_user(cls, acc_no, pin):
        for user in cls.data:
            if user["accountno"] == acc_no and user["pin"] == pin:
                return user
        return None

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Invalid age or PIN"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountno": cls.generate_account(),
            "balance": 0
        }
        cls.data.append(account)
        cls.save()
        return True, account

    @classmethod
    def deposit(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Account not found"
        if amount <= 0 or amount > 10000:
            return False, "Invalid amount"
        user["balance"] += amount
        cls.save()
        return True, user["balance"]

    @classmethod
    def withdraw(cls, acc_no, pin, amount):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Account not found"
        if amount > user["balance"]:
            return False, "Insufficient balance"
        user["balance"] -= amount
        cls.save()
        return True, user["balance"]

    @classmethod
    def update_details(cls, acc_no, pin, name, email, new_pin):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Account not found"

        user["name"] = name or user["name"]
        user["email"] = email or user["email"]
        if new_pin:
            user["pin"] = int(new_pin)

        cls.save()
        return True, "Details updated"

    @classmethod
    def delete_account(cls, acc_no, pin):
        user = cls.find_user(acc_no, pin)
        if not user:
            return False, "Account not found"
        cls.data.remove(user)
        cls.save()
        return True, "Account deleted"
