import streamlit as st
from project import Bank

st.set_page_config(page_title="Python Bank", page_icon="🏦", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.radio(
    "Select Operation",
    ["Create Account", "Deposit", "Withdraw", "Check Details", "Update Details", "Delete Account"]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):
        success, result = Bank.create_account(name, age, email, int(pin))
        if success:
            st.success("Account Created Successfully!")
            st.json(result)
        else:
            st.error(result)

# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, msg = Bank.deposit(acc, int(pin), amount)
        if success:
            st.success(f"Deposit Successful! New Balance: {msg}")
        else:
            st.error(msg)

# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, msg = Bank.withdraw(acc, int(pin), amount)
        if success:
            st.success(f"Withdraw Successful! Remaining Balance: {msg}")
        else:
            st.error(msg)

# ---------------- CHECK DETAILS ----------------
elif menu == "Check Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):
        user = Bank.find_user(acc, int(pin))
        if user:
            st.json(user)
        else:
            st.error("Account not found")

# ---------------- UPDATE DETAILS ----------------
elif menu == "Update Details":
    st.subheader("Update Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        success, msg = Bank.update_details(acc, int(pin), name, email, new_pin)
        if success:
            st.success(msg)
        else:
            st.error(msg)

# ---------------- DELETE ACCOUNT ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        success, msg = Bank.delete_account(acc, int(pin))
        if success:
            st.success(msg)
        else:
            st.error(msg)
