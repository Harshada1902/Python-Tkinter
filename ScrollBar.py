from tkinter import*
root=Tk()
sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)
mylist=Listbox(root,yscrollcommand=sb.set)
for line in range(100):
    mylist.insert(END,'This is line number'+str(line))
    mylist.pack(side=LEFT,fill=BOTH)
    sb.config(command=mylist.yview)
mainloop()
