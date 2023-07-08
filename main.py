from tkinter import *
import tkinter.ttk as ttk
import sqlite3

db_conn = sqlite3.connect("task.db")
c = db_conn.cursor()
# c.execute("""CREATE TABLE task_user(
#             task text,
#             date text
# )""")
db_conn.commit()


# db_conn.close()


def add_task():
    db_conn = sqlite3.connect("task.db")
    c = db_conn.cursor()
    c.execute("INSERT INTO task_user VALUES (:task_entry,:date_entry)",
              {
                  "task_entry": task_entry.get(),
                  "date_entry": date_entry.get(),
              }
              )
    db_conn.commit()
    db_conn.close()
    task_entry.delete(0, END)
    date_entry.delete(0, END)
    query()


def exit():
    window.destroy()


# def delete_record():
#     db_conn = sqlite3.connect("task.db")
#     c = db_conn.cursor()
#     try:
#         c.execute('DELETE FROM task_user WHERE oid='+del_)
#     except:
#     db_conn.commit()
#     db_conn.close()
def query():
    db_conn = sqlite3.connect("task.db")
    c = db_conn.cursor()
    c.execute("SELECT *, oid FROM task_user")
    records = c.fetchall()
    del_label = Label(window, text="Enter ID:", padx=5)
    del_label.grid(row=4, column=0)
    del_entry = Entry(window)
    del_entry.grid(row=4, column=1)
    del_btn = Button(window, text=" Delete Task ", bg="red")
    del_btn.grid(row=5, column=1, padx=5, pady=5)

    table = ttk.Treeview(window)
    table.grid(row=6, column=0, columnspan=2, pady=2, padx=10)
    table["columns"] = ("column 2", "column 3")
    table.column("#0", width=40, minwidth=20)
    table.column("column 2", width=70, minwidth=20)
    table.column("column 3", width=70, minwidth=20)

    table.heading("#0", text="ID", anchor=W)
    table.heading("column 2", text="Task", anchor=W)
    table.heading("column 3", text="Date", anchor=W)
    i = 0
    for record in records:
        row = table.insert("", i, text=record[2], values=(record[0], record[1]))
        i = i + 1
    db_conn.commit()
    db_conn.close()


window = Tk()
window.title("To Do List")
window.geometry("300x550")
task_label1 = Label(window, text="Enter Task :")
task_label1.grid(row=0, column=0, padx=10, pady=10)
task_label2 = Label(window, text="Enter Date :")
task_label2.grid(row=1, column=0)

task_entry = Entry(window)
task_entry.grid(row=0, column=1, columnspan=2)
date_entry = Entry(window)
date_entry.grid(row=1, column=1)
add_btn = Button(window, text="   Add Task   ", command=add_task, bg="green")
add_btn.grid(row=2, column=1, padx=5, pady=5)
show_btn = Button(window, text=" Show Tasks ", command=query)
show_btn.grid(row=3, column=1, padx=5, pady=5)
ext_btn = Button(window, text="Exit", command=exit)
ext_btn.grid(row=7, column=0, columnspan=2, ipadx=15)

window.mainloop()
