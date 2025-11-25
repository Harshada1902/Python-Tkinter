# padding at left side to a widget 
from tkinter import*
root=Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenwidth()
root.geometry("%dx%d"%(width,height))

l1=Label(root,text="Techno Savvy")
l1.grid(padx=(200,0),pady=(0,0))

root.mainloop()