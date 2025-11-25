import tkinter as tk
from tkinter import messagebox

def Login():
    username =user_entry.get()
    password=pass_entry.get()

    if username=="admin" and password=="1234":
        messagebox.showinfo("Login","Login Successfully")
    else:
        messagebox.showerror("Login","Invalid Credentials")

root=tk.Tk()
root.title("Login Window")
root.geometry("300x200")

tk.Label(root,text="Username").pack(pady=5)
user_entry=tk.Entry(root)
user_entry.pack()


tk.Label(root,text="Password").pack(pady=5)
pass_entry=tk.Entry(root)
pass_entry.pack()
tk.Button(root,text="Login",command=Login).pack(pady=10)

root.mainloop()

