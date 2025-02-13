

import tkinter as tk
from tkinter import messagebox, ttk

# Initialize the main window and student data
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x600")
root.configure(bg="#eaeaea")  # Background color changed to a light grey
students = {}

# Create UI components
frame = tk.Frame(root, bg="#f1f1f1", padx=20, pady=20)
frame.pack(pady=10, padx=10)

# Labels and Entry Fields
tk.Label(frame, text="Student ID:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
id_entry = tk.Entry(frame, font=("Arial", 18), width=40)
id_entry.pack()

tk.Label(frame, text="Student Name:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
name_entry = tk.Entry(frame, font=("Arial", 18), width=40)
name_entry.pack()

tk.Label(frame, text="Sex:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
sex_entry = tk.Entry(frame, font=("Arial", 18), width=40)
sex_entry.pack()

tk.Label(frame, text="DOB:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
dob_entry = tk.Entry(frame, font=("Arial", 18), width=40)
dob_entry.pack()

tk.Label(frame, text="Address:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
address_entry = tk.Entry(frame, font=("Arial", 18), width=40)
address_entry.pack()

tk.Label(frame, text="Result:", bg="#f1f1f1", font=("Arial", 16), fg="#333333").pack()
result_entry = tk.Entry(frame, font=("Arial", 18), width=40)
result_entry.pack()

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_style = {"font": ("Arial", 12), "width": 15, "bg": "#007BFF", "fg": "white"}

tk.Button(button_frame, text="Add Student", command=lambda: add_student(), **btn_style).grid(row=0, column=0, padx=2, pady=5)
tk.Button(button_frame, text="Show Students", command=lambda: show_students(), **btn_style).grid(row=0, column=1, padx=2, pady=5)
tk.Button(button_frame, text="Search Student", command=lambda: search_student(), **btn_style).grid(row=0, column=2, padx=2, pady=5)
tk.Button(button_frame, text="Update Student", command=lambda: update_student(), **btn_style).grid(row=0, column=3, padx=2, pady=5)
tk.Button(button_frame, text="Delete Student", command=lambda: delete_student(), **btn_style).grid(row=0, column=4, padx=2, pady=5)

# Student Table in Main Window
tree = ttk.Treeview(root, columns=("ID", "Name", "Sex", "DOB", "Address", "Result"), show="headings", style="Custom.Treeview")
tree.tag_configure("oddrow", background="#f5f5f7")  # Style for odd rows
tree.tag_configure("evenrow", background="#e0e0e0")  # Style for even rows

for col in ("ID", "Name", "Sex", "DOB", "Address", "Result"):
    tree.heading(col, text=col, anchor=tk.CENTER)
    tree.column(col, width=100, anchor=tk.CENTER)

tree.pack(fill=tk.BOTH, padx=10, pady=10)

# Styling for Treeview columns and headings
style = ttk.Style()
style.configure("Custom.Treeview", background="#f5f5f7", foreground="black", rowheight=25, font=("Arial", 12))
style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"), background="#f5f5f7", foreground="black")

def add_student():
    stu_id = id_entry.get()
    # Check if all fields are filled using 'and'
    if not stu_id or not name_entry.get() or not sex_entry.get() or not dob_entry.get() or not address_entry.get() or not result_entry.get():
        messagebox.showerror("Error", "All fields are required")
        # clear_entries()
        return  # Exit if any field is empty

    if stu_id in students:
        messagebox.showerror("Error", "Student ID already exists")
        return  # Exit if ID already exists
    else:
        students[stu_id] = {
            "Name": name_entry.get(),
            "Sex": sex_entry.get(),
            "DOB": dob_entry.get(),
            "Address": address_entry.get(),
            "Result": result_entry.get()
        }
        update_main_treeview()
        messagebox.showinfo("Success", "Student Added Successfully")
    
    clear_entries()


def update_main_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for index, (stu_id, details) in enumerate(students.items()):
        tag = "oddrow" if index % 2 == 0 else "evenrow"
        tree.insert("", "end", values=(stu_id, details["Name"], details["Sex"], details["DOB"], details["Address"], details["Result"]), tags=(tag,))

def show_students():
    popup = tk.Toplevel(root)
    popup.title("Student List")
    popup.geometry("600x400")
    student_tree = ttk.Treeview(popup, columns=("ID", "Name", "Sex", "DOB", "Address", "Result"), show="headings", style="Custom.Treeview")
    student_tree.tag_configure("oddrow", background="#f5f5f7") 
    student_tree.tag_configure("evenrow", background="#f5f5f7")
    
    for col in ("ID", "Name", "Sex", "DOB", "Address", "Result"):
        student_tree.heading(col, text=col, anchor=tk.CENTER)
        student_tree.column(col, width=100, anchor=tk.CENTER)
    
    student_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for index, (stu_id, details) in enumerate(students.items()):
        tag = "oddrow" if index % 2 == 0 else "evenrow"
        student_tree.insert("", "end", values=(stu_id, details["Name"], details["Sex"], details["DOB"], details["Address"], details["Result"]), tags=(tag,))

def search_student():
    stu_id = id_entry.get()
    if stu_id in students:
        details = students[stu_id]
        messagebox.showinfo("Student Found", f"ID: {stu_id}\nName: {details['Name']}\nSex: {details['Sex']}\nDOB: {details['DOB']}\nAddress: {details['Address']}\nResult: {details['Result']}")
    else:
        messagebox.showerror("Error", "Student Not Found")
    clear_entries()

def update_student():
    stu_id = id_entry.get()
    if stu_id not in students:  # Return early if student doesn't exist
        messagebox.showerror("Error", "Student Not Found")
        return
    students[stu_id] = {
        "Name": name_entry.get(),
        "Sex": sex_entry.get(),
        "DOB": dob_entry.get(),
        "Address": address_entry.get(),
        "Result": result_entry.get()
    }
    update_main_treeview()
    messagebox.showinfo("Success", "Student Updated Successfully")
    clear_entries()

def delete_student():
    stu_id = id_entry.get()
    if stu_id not in students:  # Return early if student doesn't exist
        messagebox.showerror("Error", "Student Not Found")
        return
    del students[stu_id]
    update_main_treeview()
    messagebox.showinfo("Success", "Student Deleted Successfully")
    clear_entries()

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    sex_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)

def on_item_double_click(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item, "values")
        clear_entries()
        id_entry.insert(0, values[0])
        name_entry.insert(0, values[1])
        sex_entry.insert(0, values[2])
        dob_entry.insert(0, values[3])
        address_entry.insert(0, values[4])
        result_entry.insert(0, values[5])

tree.bind("<Double-1>", on_item_double_click)

# Run the main loop
root.mainloop()
