from tkinter import*
root=PanedWindow()
root.pack(fill=BOTH,expand=1)
left=Entry(root,bd=5)  # bd=Breadth Size
root.add(left)
root1=PanedWindow(root,orient=VERTICAL)
root.add(root1)
top=Scale(root1,orient=HORIZONTAL)
root1.add(top)
mainloop()
