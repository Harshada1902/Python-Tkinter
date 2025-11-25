from tkinter import*
root=Tk()
var1=IntVar()
Checkbutton(root,text='Java',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(root,text='Python',variable=var2).grid(row=1,sticky=W)
var3=IntVar()
Checkbutton(root,text='PHP',variable=var3).grid(row=2,sticky=W)
mainloop()