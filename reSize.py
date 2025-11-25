from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title('Resizable')
root.geometry('250x100')
Label(root,text='It is resizable').pack(side=TOP,pady=10)
root.resizable(True,True)
mainloop()