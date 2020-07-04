from tkinter import * #while installing install with python 3 version not 2
import sqlite3

window=Tk()
window.geometry("400x150")

def login():
    print("")

def signup():
    def signup_database():
        conn=sqlite3.connect("1.db")
        cur=conn.cursor()
        cur.execute("Create table if not exists test(id INTEGER primary key,name text,email text,password text)")
        cur.execute("insert into test values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        l4=Label(signup_window,text="Account has been created",font="times 15")
        l4.grid(row=2,column=6)
        conn.commit()
        conn.close()





    window.destroy()
    signup_window=Tk()
    signup_window.geometry("400x250")
    l1=Label(signup_window,text="User-name",font="times 20")
    l1.grid(row=1,column=1)
    l2=Label(signup_window,text="Email:",font="times 20")
    l2.grid(row=2,column=1)
    l3=Label(signup_window,text="Password:",font="times 20")
    l3.grid(row=3,column=1)

    name_text=StringVar()
    e1=Entry(signup_window,textvariable=name_text)
    e1.grid(row=1,column=2)
    user_email=StringVar()
    e2=Entry(signup_window,textvariable=user_email)
    e2.grid(row=2,column=2)
    password=StringVar()
    e3=Entry(signup_window,textvariable=password)
    e3.grid(row=3,column=2)
    b1=Button(signup_window,text="Sign up",width=20,command=signup_database)
    b1.grid(row=4,column=2)
    

l1=Label(window,text="What do you want to do?",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="Log in",width=20,command=login)
b1.grid(row=2,column=2)
b2=Button(window,text="Sign up",width=20,command=signup)
b2.grid(row=2,column=3)

window.mainloop()