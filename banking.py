import tkinter as tk
from tkinter import messagebox

# A dictionary to store the user accounts (simulating a database)
accounts = {}

# Function to create a new user account
def create_user_account():
    acc_id = entry_acc_id.get()
    name = entry_name.get()
    sex = entry_sex.get()

    dob = entry_dob.get()
    pob = entry_pob.get()
    address = entry_address.get()
    balance = entry_balance.get()

    # Check if account ID already exists
    if acc_id in accounts:
        messagebox.showerror("Error", "Account ID already exists!")
        return

    # Create new account
    accounts[acc_id] = {
        "name": name,
        "sex": sex,
        "dob": dob,
        "pob": pob,
        "address": address,
        "balance": float(balance)
    }

    clear_fields()
    messagebox.showinfo("Success", "Account Created Successfully!")


# Function to check an existing user account
def check_user_account():
    acc_id = entry_acc_id.get()

    if acc_id not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    # Get user info from the account dictionary
    user_info = accounts[acc_id]
    user_details = f"Account ID: {acc_id}\nName: {user_info['name']}\nSex: {user_info['sex']}\n" \
                   f"DOB: {user_info['dob']}\nPOB: {user_info['pob']}\nAddress: {user_info['address']}\n" \
                   f"Balance: {user_info['balance']}"

    messagebox.showinfo("Account Found", user_details)


# Function to deposit money into the account
def deposit_money():
    acc_id = entry_acc_id.get()
    balance = entry_balance.get()

    if acc_id not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    if not balance.isdigit():
        messagebox.showerror("Error", "Please input your balance!")
        return

    accounts[acc_id]["balance"] += float(balance)
    clear_fields()
    messagebox.showinfo("Success", f"Deposited money successfully!")


# Function to withdraw money from the account
def withdrawal_money():
    acc_id = entry_acc_id.get()
    balance = entry_balance.get()

    if acc_id not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    if not balance.isdigit():
        messagebox.showerror("Error", "Please enter a valid amount!")
        return

    if accounts[acc_id]["balance"] < float(balance):
        messagebox.showerror("Error", "Insufficient balance!")
        return

    accounts[acc_id]["balance"] -= float(balance)
    clear_fields()
    messagebox.showinfo("Success", f"Withdrawn money successfully!")


# Function to transfer money between two accounts
def transfer_money():
    from_acc = entry_acc_id.get()
    to_acc = entry_to_acc_id.get()
    balance = entry_balance.get()

    if from_acc not in accounts:
        messagebox.showerror("Error", "From Account not found!")
        return

    if to_acc not in accounts:
        messagebox.showerror("Error", "To Account not found!")
        return

    if not balance.isdigit():
        messagebox.showerror("Error", "Please enter a valid money!")
        return

    if accounts[from_acc]["balance"] < float(balance):
        messagebox.showerror("Error", "Invalid money!")
        return

    # Perform the transfer
    accounts[from_acc]["balance"] -= float(balance)
    accounts[to_acc]["balance"] += float(balance)
    clear_fields()
    messagebox.showinfo("Success", f"Transferred {balance} from {from_acc} to {to_acc} successfully!")


# Function to update user information
def update_user_information():
    acc_id = entry_acc_id.get()
    if acc_id not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return
# Update only the fields with new values, otherwise keep the old values
    name = entry_name.get() if entry_name.get() else accounts[acc_id]["name"]
    sex = entry_sex.get() if entry_sex.get() else accounts[acc_id]["sex"]
    dob = entry_dob.get() if entry_dob.get() else accounts[acc_id]["dob"]
    pob = entry_pob.get() if entry_pob.get() else accounts[acc_id]["pob"]
    address = entry_address.get() if entry_address.get() else accounts[acc_id]["address"]
    balance = entry_balance.get() if entry_balance.get() else str(accounts[acc_id]["balance"])

    # Update the account information
    accounts[acc_id] = {
        "name": name,
        "sex": sex,
        "dob": dob,
        "pob": pob,
        "address": address,
        "balance": float(balance)
    }

    clear_fields()
    messagebox.showinfo("Success", "Account Information Updated!")


# Function to delete an existing user account
def delete_user_account():
    acc_id = entry_acc_id.get()

    if acc_id not in accounts:
        messagebox.showerror("Error", "Account not found!")
        return

    del accounts[acc_id]
    clear_fields()
    messagebox.showinfo("Success", "Account Deleted Successfully!")


# Function to clear all input fields
def clear_fields():
    entry_acc_id.delete(0,tk.END)
    entry_name.delete(0, tk.END)
    entry_sex.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_pob.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_balance.delete(0, tk.END)
    entry_to_acc_id.delete(0, tk.END)


# Setting up the Tkinter window
root = tk.Tk()
root.title("User information")

# Labels and entry fields for account information
tk.Label(root, text="Account ID").grid(row=0, column=0)
entry_acc_id = tk.Entry(root)
entry_acc_id.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Sex").grid(row=2, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=2, column=1)

tk.Label(root, text="Date of Birth").grid(row=3, column=0)
entry_dob = tk.Entry(root)
entry_dob.grid(row=3, column=1)

tk.Label(root, text="Place of Birth").grid(row=4, column=0)
entry_pob = tk.Entry(root)
entry_pob.grid(row=4, column=1)

tk.Label(root, text="Address").grid(row=5, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=5, column=1)

tk.Label(root, text="Balance").grid(row=6, column=0)
entry_balance = tk.Entry(root)
entry_balance.grid(row=6, column=1)

tk.Label(root, text="To Account ID (for Transfer)").grid(row=7, column=0)
entry_to_acc_id = tk.Entry(root)
entry_to_acc_id.grid(row=7, column=1)

# Buttons for each action
tk.Button(root, text="Create Account", command=create_user_account).grid(row=8, column=0)
tk.Button(root, text="Check Account", command=check_user_account).grid(row=8, column=1)
tk.Button(root, text="Deposit Money", command=deposit_money).grid(row=9, column=0)
tk.Button(root, text="Withdraw Money", command=withdrawal_money).grid(row=9, column=1)
tk.Button(root, text="Transfer Money", command=transfer_money).grid(row=10, column=0)
tk.Button(root, text="Update Account", command=update_user_information).grid(row=10, column=1)
tk.Button(root, text="Delete Account", command=delete_user_account).grid(row=11, column=0)
tk.Button(root, text="Exit", command=root.quit).grid(row=11, column=1)

# Start the Tkinter event loop
root.mainloop()