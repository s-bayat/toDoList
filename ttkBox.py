from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry("300x500")
table = ttk.Treeview(root)
table.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
table["columns"] = ("column 2", "column 3")
table.column("#0", width=50, minwidth=20)
table.column("column 2", width=90, minwidth=20)
table.column("column 3", width=90, minwidth=20)

root.mainloop()
