from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ems import Database

# Initialize Database
db = Database("Employee.db")

root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")

# Variables
name = StringVar()
code = StringVar()
email = StringVar()
contact = StringVar()
gender = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#5dade2")
entries_frame.pack(side=TOP, fill=X)

# Title
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=4, padx=10, pady=20, sticky="w")

# Labels and Entry fields
Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

Label(entries_frame, text="Employee Code", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtCode = Entry(entries_frame, textvariable=code, font=("Calibri", 16), width=30)
txtCode.grid(row=1, column=3, padx=10, pady=10, sticky="w")

Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=2, column=1, padx=10, pady=10, sticky="w")

Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
txtContact.grid(row=2, column=3, padx=10, pady=10, sticky="w")

# Gender Field
Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
frame_gender = Frame(entries_frame, bg="#5dade2")
frame_gender.grid(row=3, column=1, padx=10, pady=10, sticky="w")

Radiobutton(frame_gender, text="Male", variable=gender, value="Male", font=("Calibri", 16), bg="#5dade2", fg="white").pack(side=LEFT)
Radiobutton(frame_gender, text="Female", variable=gender, value="Female", font=("Calibri", 16), bg="#5dade2", fg="white").pack(side=LEFT)
Radiobutton(frame_gender, text="Other", variable=gender, value="Other", font=("Calibri", 16), bg="#5dade2", fg="white").pack(side=LEFT)

# Address Field
Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
txtAddress.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="w")


# Functions
def getData(event):
    selected_row = tv.focus()
    if not selected_row:  # Check if any row is selected
        return
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    code.set(row[2])
    email.set(row[3])
    contact.set(row[4])
    gender.set(row[5])  # Fixed index to match gender column
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[6])  # Fixed index to match address column

def delete_employee():
    if not row:
        messagebox.showerror("Error", "No record selected")
        return
    db.remove(row[0])
    clearAll()
    displayAll()

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def update_employee():
    if not row:
        messagebox.showerror("Error", "No record selected")
        return
    if txtName.get() == "" or txtCode.get() == "" or txtEmail.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END).strip() == "" or gender.get() == "":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.update(row[0], txtName.get(), txtCode.get(), txtEmail.get(), txtContact.get(), gender.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()

def add_employee():
    if txtName.get() == "" or txtCode.get() == "" or txtEmail.get() == "" or txtContact.get() == "" or txtAddress.get(1.0, END).strip() == "" or gender.get() == "":
        messagebox.showerror("Error in Input", "Please fill all the details")
        return
    db.insert(txtName.get(), txtCode.get(), txtEmail.get(), txtContact.get(), gender.get(), txtAddress.get(1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    code.set("")
    email.set("")
    contact.set("")
    gender.set("") 
    txtAddress.delete(1.0, END)
    global row
    row = None  

# Buttons
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")

Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)
Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#16a085", bd=0).grid(row=0, column=0)
Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)
Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"), fg="white", bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)
# Table frame with Scrollbars
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)

# Scrollbars
scroll_y = Scrollbar(tree_frame, orient=VERTICAL)
scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)

style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 18))

# Treeview configuration
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7,8), style="mystyle.Treeview", yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Define Columns
tv.heading(1, text="ID")
tv.column(1, width=60)

tv.heading(2, text="Name")
tv.column(2, width=100)

tv.heading(3, text="Code")
tv.column(3, width=100)

tv.heading(4, text="Email")
tv.column(4, width=200)

tv.heading(5, text="Contact")
tv.column(5, width=100)

tv.heading(6, text="Gender")
tv.column(6, width=100)

tv.heading(7, text="Address")
tv.column(7, width=500)

tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=BOTH, expand=1)

# Display all records initially
displayAll()

root.mainloop()
