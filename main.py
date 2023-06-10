from tkinter import *

window = Tk()
window.title("To Do List")
window.geometry("300x500")
task_label1 = Label(window, text="Enter Task :")
task_label1.grid(row=0, column=0)
task_label2 = Label(window, text="Enter Date :")
task_label2.grid(row=1, column=0)

window.mainloop()
