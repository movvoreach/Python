import tkinter as tk
from tkinter import messagebox

# Dictionary to store user accounts
accounts = {}

# Function to create a new user account
def create_user_account():
    user_id = id_entry.get()

    if user_id in accounts:
        messagebox.showerror("Error", "User ID already exists!")
        return

    accounts[user_id] = {
        "name": name_entry.get(),
        "sex": sex_entry.get(),
        "dob": dob_entry.get(),
        "pob": pob_entry.get(),
        "address": address_entry.get(),
        "balance": 0,
    }
    messagebox.showinfo("Success", "Account created successfully!")
    clear_entries()

# Function to check user account
def check_user_account():
    user_id = id_entry.get()
    if user_id not in accounts:
        messagebox.showerror("Error", "User ID not found!")
        return
    account = accounts[user_id]
    details = (
        f"ID: {user_id}\n"
        f"Name: {account['name']}\n"
        f"Sex: {account['sex']}\n"
        f"DOB: {account['dob']}\n"
        f"POB: {account['pob']}\n"
        f"Address: {account['address']}\n"
        f"Balance: {account['balance']}"
    )
    messagebox.showinfo("Account Details", details)

# Function to deposit money
def deposit_money():
    user_id = id_entry.get()
    if user_id in accounts:
        try:
            new_balance = float(amount_entry.get())
            accounts[user_id]["balance"] += new_balance
            messagebox.showinfo("Success", f"Deposited {new_balance} successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount!")
    else:
        messagebox.showerror("Error", "User ID not found!")
    clear_entries()

# Function to withdraw money
def withdraw_money():
    user_id = id_entry.get()
    if user_id not in accounts:
        messagebox.showerror("Error", "User ID not found!")
        return
    try:
        amount = float(amount_entry.get())
        if accounts[user_id]["balance"] >= amount:
            accounts[user_id]["balance"] -= amount
            messagebox.showinfo("Success", f"Withdrawn {amount} successfully!")
        else:
            messagebox.showerror("Error", "Insufficient balance!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount!")
    clear_entries()

# Function to transfer money
def transfer_money():
    from_id = id_entry.get()
    to_id = transfer_to_entry.get()
    if from_id not in accounts or to_id not in accounts:
        messagebox.showerror("Error", "Invalid User ID(s)!")
        return
    try:
        amount = float(amount_entry.get())
        if accounts[from_id]["balance"] >= amount:
            accounts[from_id]["balance"] -= amount
            accounts[to_id]["balance"] += amount
            messagebox.showinfo("Success", f"Transferred {amount} successfully!")
        else:
            messagebox.showerror("Error", "Insufficient balance!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount!")
    clear_entries()

# Function to update user information
def update_user_information():
    user_id = id_entry.get()
    if user_id not in accounts:
        messagebox.showerror("Error", "User ID not found!")
        return
    accounts[user_id]["name"] = name_entry.get() or accounts[user_id]["name"]
    accounts[user_id]["sex"] = sex_entry.get() or accounts[user_id]["sex"]
    accounts[user_id]["dob"] = dob_entry.get() or accounts[user_id]["dob"]
    accounts[user_id]["pob"] = pob_entry.get() or accounts[user_id]["pob"]
    accounts[user_id]["address"] = address_entry.get() or accounts[user_id]["address"]
    messagebox.showinfo("Success", "User information updated!")
    clear_entries()

# Function to delete user account
def delete_user_account():
    user_id = id_entry.get()
    if user_id in accounts:
        del accounts[user_id]
        messagebox.showinfo("Success", "User account deleted!")
    else:
        messagebox.showerror("Error", "User ID not found!")
    clear_entries()

# Function to clear entry fields
def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    pob_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    transfer_to_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Banking Management System")

# Labels and entry fields
tk.Label(root, text="User ID").grid(row=0, column=0, padx=10, pady=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Sex").grid(row=2, column=0, padx=10, pady=5)
sex_entry = tk.Entry(root)
sex_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="DOB").grid(row=3, column=0, padx=10, pady=5)
dob_entry = tk.Entry(root)
dob_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="POB").grid(row=4, column=0, padx=10, pady=5)
pob_entry = tk.Entry(root)
pob_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=5, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Amount").grid(row=6, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Transfer To (ID)").grid(row=7, column=0, padx=10, pady=5)
transfer_to_entry = tk.Entry(root)
transfer_to_entry.grid(row=7, column=1, padx=10, pady=5)

# Buttons for functionalities
tk.Button(root, text="Create Account", command=create_user_account, bg="lightgreen").grid(row=8, column=0, pady=10)
tk.Button(root, text="Check Account", command=check_user_account).grid(row=8, column=1, pady=10)
tk.Button(root, text="Deposit Money", command=deposit_money, bg="lightyellow").grid(row=9, column=0, pady=10)
tk.Button(root, text="Withdraw Money", command=withdraw_money, bg="lightpink").grid(row=9, column=1, pady=10)
tk.Button(root, text="Transfer Money", command=transfer_money, bg="blue").grid(row=10, column=0, pady=10)
tk.Button(root, text="Update Info", command=update_user_information, bg="orange").grid(row=10, column=1, pady=10)
tk.Button(root, text="Delete Account", command=delete_user_account, bg="red").grid(row=11, column=0, pady=10)
tk.Button(root, text="Exit", command=root.quit, bg="black", fg="white").grid(row=11, column=1, pady=10)

# Run the application
root.mainloop()
 