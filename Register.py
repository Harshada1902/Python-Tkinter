from tkinter import *

root = Tk()
root.title("Registration Form")

Label(root, text='First Name').grid(row=0, column=0, sticky=W)
Entry(root).grid(row=0, column=1)

Label(root, text='Last Name').grid(row=1, column=0, sticky=W)
Entry(root).grid(row=1, column=1)

Label(root, text='Address').grid(row=2, column=0, sticky=W)
Entry(root).grid(row=2, column=1)

Label(root, text='Email').grid(row=3, column=0, sticky=W)
Entry(root).grid(row=3, column=1)

Label(root, text='Gender').grid(row=4, column=0, sticky=W)
var = IntVar()
Radiobutton(root, text='Male', variable=var, value=1).grid(row=4, column=1, sticky=W)
Radiobutton(root, text='Female', variable=var, value=2).grid(row=5, column=1, sticky=W)

Label(root, text='Subjects').grid(row=6, column=0, sticky=W)
var1 = IntVar()
Checkbutton(root, text='Java', variable=var1).grid(row=6, column=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text='Python', variable=var2).grid(row=7, column=1, sticky=W)
var3 = IntVar()
Checkbutton(root, text='PHP', variable=var3).grid(row=8, column=1, sticky=W)

Button(root, text='Register').grid(row=9, column=1)

root.mainloop()
