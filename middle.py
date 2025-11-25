# we can use place() method to set the position of the Tkinter Label
import tkinter as tk
root=tk.Tk()
Label_mid=tk.Label(root,text='Middle')
Label_mid.place(relx=0.5,rely=0.5,anchor='center')

Lower_Left=tk.Label(root,text='Lower Left')
Lower_Left.place(relx=0.0,rely=1.0,anchor='sw')

Lower_Right=tk.Label(root,text="Lower Right")
Lower_Right.place(relx=1.0,rely=0.0,anchor='ne')


root.mainloop()








