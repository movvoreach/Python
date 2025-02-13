import tkinter as tk
from tkinter import ttk,messagebox

# In-memory database to store user data
user_ids = set()  # Set to store unique user IDs
users_db = []     # List to store user data (dictionaries)

# Function to create a user account
def create_user_account():
    user_id = entry_user_id.get()
    name = entry_name.get()
    dob = entry_dob.get()
    pob = entry_pob.get()
    sex = entry_sex.get()
    address = entry_address.get()
    balance = entry_balance.get()
    # if balance.isdigit() else 0
    if user_id and name and dob and pob and sex and address and balance:
        if user_id not in user_ids:
            user_ids.add(user_id)

            balance = int(balance) 

            user_data = {
                'user_id': user_id,
                'name': name,
                'dob': dob,
                'pob': pob,
                'sex': sex,
                'address': address,
                'balance': balance
            }
            users_db.append(user_data)
            messagebox.showinfo("Success", f"Account created for {name}")
        else:
            messagebox.showwarning("Error", "User ID already exists")
    else:
        messagebox.showwarning("Error", "Please fill all fields")

# Function to check user account details
def check_user_account():
    user_id = entry_user_id.get()
    for user in users_db:
        if user['user_id'] == user_id:
            messagebox.showinfo("Account Info", 
                f"Name: {user['name']}\nDOB: {user['dob']}\nPOB: {user['pob']}\nAddress: {user['address']}\nBalance: ${user['balance']}")
            return
    messagebox.showwarning("Error", "User not found")

# Function to deposit money into a user's account
def deposit_money():
    user_id = entry_user_id.get()
    amount = entry_amount.get()
    for user in users_db:
        if user['user_id'] == user_id:
            if int(amount) >= 0:
                user['balance'] += int(amount)
                messagebox.showinfo("Success", f"Deposited ${amount}. New balance: ${user['balance']}")
                return
            else:
                messagebox.showwarning("Error", "Please enter a valid deposit amount")
                return
    messagebox.showwarning("Error", "User not found")

# Function to withdraw money from a user's account
def withdraw_money():
    user_id = entry_user_id.get()
    amount = entry_amount.get()
    for user in users_db:
        if user['user_id'] == user_id:
            if int(amount) > 0:
                if user['balance'] >= int(amount):
                    user['balance'] -= int(amount)
                    messagebox.showinfo("Success", f"Withdrew ${amount}. New balance: ${user['balance']}")
                    return
                else:
                    messagebox.showwarning("Error", "Insufficient funds")
                    return
            else:
                messagebox.showwarning("Error", "Please enter a valid withdrawal amount")
                return
    messagebox.showwarning("Error", "User not found")

# Function to transfer money between users
def transfer_money():
    sender_id = entry_user_id.get()
    recipient_id = entry_recipient_id.get()
    amount = entry_amount.get()
    sender = ''
    recipient = ''
    for user in users_db:
        if user['user_id'] == sender_id:
            sender = user
        if user['user_id'] == recipient_id:
            recipient = user
    if sender and recipient:
        if int(amount) > 0:
            amount = int(amount)
            if sender['balance'] >= amount:
                sender['balance'] -= amount
                recipient['balance'] += amount
                messagebox.showinfo("Success", f"Transferred ${amount} to {recipient['name']}. New balance: ${sender['balance']}")
            else:
                messagebox.showwarning("Error", "Insufficient funds")
        else:
            messagebox.showwarning("Error", "Please enter a valid transfer amount")
    else:
        messagebox.showwarning("Error", "Sender or  recipient not found")

# Function to update user information
def update_user_information():
    user_id = entry_user_id.get()
    newname = entry_name.get()
    newdob = entry_dob.get()
    newpob = entry_pob.get()
    newsex = entry_sex.get()
    new_address = entry_address.get()
    for user in users_db:
        if user['user_id'] == user_id:
            user['address'] = new_address
            user['name'] = newname
            user['dob'] = newdob
            user['pob'] = newpob
            user['sex'] = newsex
            messagebox.showinfo("Success", f"Updated address for {user['name']}")
            return
    messagebox.showwarning("Error", "User not found")

# Function to delete a user account
def delete_user():
    user_id = entry_user_id.get()
    for user in users_db:
        if user['user_id'] == user_id:
            users_db.remove(user)
            user_ids.remove(user_id)
            messagebox.showinfo("Success", f"Account for {user['name']} deleted")
            return
    messagebox.showwarning("Error", "User not found")

# Function to clear all input fields
def clear_fields():
    entry_user_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_pob.delete(0, tk.END)
    entry_sex.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_balance.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_recipient_id.delete(0, tk.END)

# Create main window
window = tk.Tk()
window.title("Banking System Management")
window.geometry("600x500")  # Adjust window size

# Set background color
window.config(bg="#4CAF50")  # green background for a modern look


# Styling for modern look
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 10), padding=5, background="#f4f4f9")
style.configure('TButton', font=('Helvetica', 10, 'bold'), padding=8, relief="flat", background="#FF0000", foreground="white")
# style.map('TButton', background=[('active', '#0000FF')])  # Red background, blue when active
style.configure('TEntry', font=('Helvetica', 10), padding=5)
style.theme_use("clam")


# Define labels and entry fields for user input
ttk.Label(window, text="User ID").grid(row=0, column=0)
entry_user_id = ttk.Entry(window)
entry_user_id.grid(row=0, column=1)

ttk.Label(window, text="Name").grid(row=1, column=0)
entry_name = ttk.Entry(window)
entry_name.grid(row=1, column=1)

ttk.Label(window, text="Date of Birth").grid(row=2, column=0)
entry_dob = ttk.Entry(window)
entry_dob.grid(row=2, column=1)

ttk.Label(window, text="Place of Birth").grid(row=3, column=0)
entry_pob = ttk.Entry(window)
entry_pob.grid(row=3, column=1)

ttk.Label(window, text="Sex").grid(row=4, column=0)
entry_sex = ttk.Entry(window)
entry_sex.grid(row=4, column=1)

ttk.Label(window, text="Address").grid(row=5, column=0)
entry_address = ttk.Entry(window)
entry_address.grid(row=5, column=1)

ttk.Label(window, text="Balance").grid(row=6, column=0)
entry_balance = ttk.Entry(window)
entry_balance.grid(row=6, column=1)

ttk.Label(window, text="Amount").grid(row=7, column=0)
entry_amount = ttk.Entry(window)
entry_amount.grid(row=7, column=1)

ttk.Label(window, text="Recipient ID (for Transfer)").grid(row=8, column=0)
entry_recipient_id = ttk.Entry(window)
entry_recipient_id.grid(row=8, column=1)

# Buttons for different actions in the banking system
ttk.Button(window, text="Create Account", command=create_user_account).grid(row=9, column=0, padx=10, pady=10)
ttk.Button(window, text="Check Account", command=check_user_account).grid(row=9, column=1, padx=10, pady=10)
ttk.Button(window, text="Deposit Money", command=deposit_money).grid(row=10, column=0, padx=10, pady=10)
ttk.Button(window, text="Withdraw Money", command=withdraw_money).grid(row=10, column=1, padx=10, pady=10)
ttk.Button(window, text="Transfer Money", command=transfer_money).grid(row=11, column=0, padx=10, pady=10)
ttk.Button(window, text="Update Info", command=update_user_information).grid(row=11, column=1, padx=10, pady=10)
ttk.Button(window, text="Delete Account", command=delete_user).grid(row=12, column=0, padx=10, pady=10)
ttk.Button(window, text="Clear Fields", command=clear_fields).grid(row=12, column=1, padx=10, pady=10)

# Run the application
window.mainloop()
