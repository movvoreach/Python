import tkinter as tk
from tkinter import messagebox

# In-memory database to store user data
user_ids = set()  # Set to store unique user IDs
users_db = []     # List to store user data (dictionaries)

# Functions (same as before, omitted for brevity)

# Function to create a modern button style
def create_custom_button(parent, text, command):
    return tk.Button(
        parent,
        text=text,
        command=command,
        bg="#4CAF50",  # Green background
        fg="white",    # White text
        font=("Helvetica", 10, "bold"),
        relief="flat",  # Flat button style
        activebackground="#45a049",  # Slightly darker green when pressed
        activeforeground="white",    # White text when pressed
        padx=8, pady=5               # Padding for a modern look
    )

# GUI Setup
window = tk.Tk()
window.title("Banking System Management")
window.geometry("600x500")  # Adjust window size
window.config(bg="#f4f4f9")  # Light grey background for a modern look

# Define labels and entry fields for user input
def create_label_entry(parent, text, row):
    tk.Label(
        parent,
        text=text,
        bg="#f4f4f9",  # Match the window background color
        font=("Helvetica", 10),
        anchor="w"
    ).grid(row=row, column=0, sticky="w", padx=10, pady=5)
    entry = tk.Entry(parent, font=("Helvetica", 10), width=30)
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

entry_user_id = create_label_entry(window, "User ID", 0)
entry_name = create_label_entry(window, "Name", 1)
entry_dob = create_label_entry(window, "Date of Birth", 2)
entry_pob = create_label_entry(window, "Place of Birth", 3)
entry_sex = create_label_entry(window, "Sex", 4)
entry_address = create_label_entry(window, "Address", 5)
entry_balance = create_label_entry(window, "Balance", 6)
entry_amount = create_label_entry(window, "Amount", 7)
entry_recipient_id = create_label_entry(window, "Recipient ID (for Transfer)", 8)

# Buttons for different actions
button_frame = tk.Frame(window, bg="#f4f4f9")  # Frame to organize buttons
button_frame.grid(row=9, column=0, columnspan=2, pady=10)

buttons = [
    ("Create Account", create_user_account),
    ("Check Account", check_user_account),
    ("Deposit Money", deposit_money),
    ("Withdraw Money", withdraw_money),
    ("Transfer Money", transfer_money),
    ("Update Info", update_user_information),
    ("Clear Fields", clear_fields),
    ("Delete Account", delete_user),
]

for i, (text, command) in enumerate(buttons):
    btn = create_custom_button(button_frame, text, command)
    btn.grid(row=i // 2, column=i % 2, padx=10, pady=5, sticky="ew")

# Start the application window
window.mainloop()
