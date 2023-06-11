from tkinter import *
from tkinter import ttk

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
window.mainloop()
