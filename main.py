from tkinter import *
import tkinter.ttk as ttk
import sqlite3

def add_task():
    


window = Tk()
window.title("To Do List")
window.geometry("300x500")
task_label1 = Label(window, text="Enter Task :")
task_label1.grid(row=0, column=0, padx=10, pady=10)
task_label2 = Label(window, text="Enter Date :")
task_label2.grid(row=1, column=0)
task_entry = Entry(window)
task_entry.grid(row=0, column=1)
date_entry = Entry(window)
date_entry.grid(row=1, column=1)
add_btn = Button(window, text="   Add Task   ", command=addtask)
add_btn.grid(row=2, column=1, padx=5, pady=5)
del_btn = Button(window, text=" Delete Task ")
del_btn.grid(row=3, column=1, padx=5, pady=5)
table = ttk.Treeview(window)
table.grid(row=4, column=0, columnspan=3, pady=10, padx=30)
table["columns"] = ("column 2", "column 3")
table.column("#0", width=50, minwidth=20)
table.column("column 2", width=90, minwidth=20)
table.column("column 3", width=90, minwidth=20)

table.heading("#0", text="ID", anchor=W)
table.heading("column 2", text="Task", anchor=W)
table.heading("column 3", text="Date", anchor=W)

window.mainloop()
