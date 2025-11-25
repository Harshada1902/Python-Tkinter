from tkinter import*
root=Tk()
var=IntVar()
Radiobutton(root,text='Male',variable=var,value=1).pack(anchor=W)
Radiobutton(root,text='Female',variable=var,value=2).pack(anchor=W)
mainloop()