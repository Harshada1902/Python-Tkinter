import tkinter as tk
root=tk.Tk()
root.title("Color Option in tkinter")

button=tk.Button(root,text="Click Me",activebackground="yellow",activeforeground="black")
button.pack()
label=tk.Label(root,text="Hello! Tkinter",bg="red",fg="black")
label.pack()

entry=tk.Entry(root,selectbackground="blue",selectforeground="black")
entry.pack()
root.mainloop()
