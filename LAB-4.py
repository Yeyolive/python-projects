import tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.amount = 0
    def deposit(self):
        i = (int)(self.en.get())
        if(i>0):
            self.amount += i
            self.en.delete(0, 'end')
            self.lab.config(text="Succeessfully deposited {}".format(i))
        else:
            self.en.delete(0, 'end')
            self.lab.config(text="Error occured try again")
    def show(self):
        print(self.amount)
        self.lab.config(text="you have {}".format(self.amount))
    def withdraw(self):
        i = (int)(self.en.get())
        self.en.delete(0, 'end')
        if(i<self.amount):
            self.amount -= i
            self.lab.config(text="Succeessfully withdrawed {}".format(self.amount))
        else:
            self.lab.config(text="You dont have sufficient amount")
    def create_widgets(self):
        self.head = tk.Label(self,text="Welcome to Bank",font=("Courier", 25))
        self.head.grid(row=0,column=1)
        self.a = tk.Button(self, text ="Show"   , width=10, height=2, command=self.show)
        self.b = tk.Button(self, text="Deposit", width=10, height=2, command=self.deposit)
        self.c = tk.Button(self, text="Withdraw", width=10, height=2, command=self.withdraw)
        self.a.grid(row=1,column=0)
        self.c.grid(row=1,column=1)
        self.b.grid(row=1,column=2)
        self.enlab = tk.Label(self,text="Enter amount:",font=("Courier", 20));
        self.enlab.grid(row=2,column=0)
        self.en = tk.Entry(self)
        self.en.grid(row=2,column=1)
        self.lab = tk.Label(self,font=("Courier", 20));
        self.lab.grid(row=3,column=1)
root = tk.Tk()
app = Application(master=root)
app.master.title("Bank Application")
app.master.maxsize(800, 400)
app.master.minsize(800, 400)
app.grid_rowconfigure(4,minsize=20)
app.mainloop()
