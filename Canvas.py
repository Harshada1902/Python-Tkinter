from tkinter import*
root=Tk()
w=Canvas(root,width=400,height=600)
w.pack()

w.create_line(50,50,200,50,fill="red",width=3)
w.create_oval(250,80,400,150,fill="lightgreen",outline="blue",width=2)
w.create_rectangle(50,80,200,150,fill="lightblue",outline="blue",width=2)
w.create_polygon(150,200,50,300,fill="violet",outline="purple",width=2)
w.create_arc(300,200,450,350,start=0,extent=150,fill="orange")
mainloop()