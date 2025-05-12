from tkinter import *


def add():
    a = float(e1.get())
    b = float(e2.get())
    answer = a + b
    r1.configure(text=str(answer))


def sub():
    a = float(e1.get())
    b = float(e2.get())
    answer = a - b
    r1.configure(text=str(answer))


def mul():
    a = float(e1.get())
    b = float(e2.get())
    answer = a * b
    r1.configure(text=str(answer))


def div():
    a = float(e1.get())
    b = float(e2.get())
    answer = a / b
    r1.configure(text=str(answer))


tk = Tk()
tk.title("Calculator")
tk.geometry('500x250')
l1 = Label(text='Enter first number')
l1.grid(row=0, column=0, padx=10, pady=10)
e1 = Entry()
e1.grid(row=0, column=1)

l2 = Label(text='Enter second number')
l2.grid(row=1, column=0, padx=10, pady=10)
e2 = Entry()
e2.grid(row=1, column=1)

b1 = Button(text='+', command=add)
b1.grid(row=2, column=0, pady=10)
b2 = Button(text='-', command=sub)
b2.grid(row=2, column=1, pady=10)
b3 = Button(text='*', command=mul)
b3.grid(row=3, column=0, pady=10)
b4 = Button(text='/', command=div)
b4.grid(row=3, column=1, pady=10)

r = Label(text='Result')
r.grid(row=4, column=0, padx=10, pady=10)
r1 = Label(text='')
r1.grid(row=4, column=1)

tk.resizable(False, False)
tk.mainloop()
