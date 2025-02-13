import tkinter as tk
from tkinter import messagebox, ttk

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")
        
        self.students = {}
        self.current_index = 0  # Track current student index for show_students
        
        # Labels and Entry Fields with Styling
        frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, borderwidth=2)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(frame, text="Student ID:", bg="#ffffff", font=("Arial", 12)).pack()
        self.id_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.id_entry.pack()
        
        tk.Label(frame, text="Name:", bg="#ffffff", font=("Arial", 12)).pack()
        self.name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.name_entry.pack()
        
        tk.Label(frame, text="Sex:", bg="#ffffff", font=("Arial", 12)).pack()
        self.sex_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.sex_entry.pack()
        
        tk.Label(frame, text="DOB:", bg="#ffffff", font=("Arial", 12)).pack()
        self.dob_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.dob_entry.pack()
        
        tk.Label(frame, text="Address:", bg="#ffffff", font=("Arial", 12)).pack()
        self.address_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.address_entry.pack()
        
        tk.Label(frame, text="Result:", bg="#ffffff", font=("Arial", 12)).pack()
        self.result_entry = tk.Entry(frame, font=("Arial", 12), width=30)
        self.result_entry.pack()
        
        # Navigation Buttons for Show Students
        nav_frame = tk.Frame(frame, bg="#ffffff")
        nav_frame.pack(pady=5)
        
        btn_style = {"font":("Arial", 10), "width":10, "bg":"#4CAF50", "fg":"white", "bd":2}
        
        self.prev_btn = tk.Button(nav_frame, text="Previous", command=self.show_previous, **btn_style)
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        self.next_btn = tk.Button(nav_frame, text="Next", command=self.show_next, **btn_style)
        self.next_btn.pack(side=tk.LEFT, padx=5)
        
        # Main Buttons with Styling
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=10)
        
        main_btn_style = {"font":("Arial", 12), "width":15, "bg":"#4CAF50", "fg":"white", "bd":2, "activebackground":"#45a049"}
        
        tk.Button(button_frame, text="Add Student", command=lambda: self.handle_button_click(self.add_student), **main_btn_style).grid(row=0, column=0, padx=2, pady=5)
        tk.Button(button_frame, text="Show Students", command=lambda: self.handle_button_click(self.show_students), **main_btn_style).grid(row=0, column=1, padx=2, pady=5)
        tk.Button(button_frame, text="Search Student", command=lambda: self.handle_button_click(self.search_student), **main_btn_style).grid(row=0, column=2, padx=2, pady=5)
        tk.Button(button_frame, text="Update Student", command=lambda: self.handle_button_click(self.update_student), **main_btn_style).grid(row=0, column=3, padx=2, pady=5)
        tk.Button(button_frame, text="Delete Student", command=lambda: self.handle_button_click(self.delete_student), **main_btn_style).grid(row=0, column=4, padx=2, pady=5)
        
        # Student List Display with Styling
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Sex", "DOB", "Address", "Result"), show="headings")
        for col in ("ID", "Name", "Sex", "DOB", "Address", "Result"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Bind double-click event to populate entry fields
        self.tree.bind("<Double-1>", self.on_item_double_click)
        
    def handle_button_click(self, func):
        """Wrapper for button clicks to clear entries after operation"""
        func()
        self.clear_entries()
    
    def add_student(self):
        stu_id = self.id_entry.get()
        if not stu_id:
            messagebox.showerror("Error", "Student ID is required")
            return
        if stu_id in self.students:
            messagebox.showerror("Error", "Student ID already exists")
            return
        self.students[stu_id] = {
            "Name": self.name_entry.get(),
            "Sex": self.sex_entry.get(),
            "DOB": self.dob_entry.get(),
            "Address": self.address_entry.get(),
            "Result": self.result_entry.get()
        }
        self.update_tree_view()
        messagebox.showinfo("Success", "Student Added Successfully")
    
    def show_students(self):
        if not self.students:
            messagebox.showinfo("Info", "No students to display")
            return
            
        # Convert dictionary to list for easier navigation
        self.student_list = list(self.students.items())
        self.current_index = 0
        self.display_current_student()
        self.update_navigation_buttons()
        self.update_tree_view()
    
    def show_previous(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_current_student()
            self.update_navigation_buttons()
    
    def show_next(self):
        if self.current_index < len(self.student_list) - 1:
            self.current_index += 1
            self.display_current_student()
            self.update_navigation_buttons()
    
    def display_current_student(self):
        if hasattr(self, 'student_list') and self.student_list:
            stu_id, details = self.student_list[self.current_index]
            self.clear_entries()
            self.id_entry.insert(0, stu_id)
            self.name_entry.insert(0, details["Name"])
            self.sex_entry.insert(0, details["Sex"])
            self.dob_entry.insert(0, details["DOB"])
            self.address_entry.insert(0, details["Address"])
            self.result_entry.insert(0, details["Result"])
    
    def update_navigation_buttons(self):
        self.prev_btn.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if self.current_index < len(self.student_list) - 1 else tk.DISABLED)
    
    def update_tree_view(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for stu_id, details in self.students.items():
            self.tree.insert("", "end", values=(stu_id, details["Name"], details["Sex"], 
                                              details["DOB"], details["Address"], details["Result"]))
    
    def search_student(self):
        stu_id = self.id_entry.get()
        if not stu_id:
            messagebox.showerror("Error", "Please enter Student ID to search")
            return
        if stu_id in self.students:
            details = self.students[stu_id]
            self.clear_entries()
            self.id_entry.insert(0, stu_id)
            self.name_entry.insert(0, details["Name"])
            self.sex_entry.insert(0, details["Sex"])
            self.dob_entry.insert(0, details["DOB"])
            self.address_entry.insert(0, details["Address"])
            self.result_entry.insert(0, details["Result"])
        else:
            messagebox.showerror("Error", "Student Not Found")
    
    def update_student(self):
        stu_id = self.id_entry.get()
        if not stu_id:
            messagebox.showerror("Error", "Please enter Student ID to update")
            return
        if stu_id in self.students:
            self.students[stu_id] = {
                "Name": self.name_entry.get(),
                "Sex": self.sex_entry.get(),
                "DOB": self.dob_entry.get(),
                "Address": self.address_entry.get(),
                "Result": self.result_entry.get()
            }
            self.update_tree_view()
            messagebox.showinfo("Success", "Student Updated Successfully")
        else:
            messagebox.showerror("Error", "Student Not Found")
    
    def delete_student(self):
        stu_id = self.id_entry.get()
        if not stu_id:
            messagebox.showerror("Error", "Please enter Student ID to delete")
            return
        if stu_id in self.students:
            del self.students[stu_id]
            self.update_tree_view()
            messagebox.showinfo("Success", "Student Deleted Successfully")
        else:
            messagebox.showerror("Error", "Student Not Found")
    
    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.sex_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)
    
    def on_item_double_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            self.clear_entries()
            self.id_entry.insert(0, values[0])
            self.name_entry.insert(0, values[1])
            self.sex_entry.insert(0, values[2])
            self.dob_entry.insert(0, values[3])
            self.address_entry.insert(0, values[4])
            self.result_entry.insert(0, values[5])

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()