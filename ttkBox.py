from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry("300x500")
table = ttk.Treeview(root)
table.grid(row=0, column=0, columnspan=3, pady=5, padx=3)
table["columns"] = ("column 2", "column 3")
table.column("#0", width=20, minwidth=20)
table.column("column 2", width=40, minwidth=20)
table.column("column 3", width=40, minwidth=20)

root.mainloop()
