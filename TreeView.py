from tkinter import*
from tkinter import ttk
root=Tk()
root.title("Application Of Python")
ttk.Label(root,text="Treeview(hierarchical)").pack()
# Create treeview window
treeview=ttk.Treeview(root)
# Calling pack method
treeview.pack()
# insert Parent element in treeview
treeview.insert('','0','item1',text="TechnoSavy")
# insert child
treeview.insert('','1','item2',text="Computer Science")
treeview.insert('','2','item3',text="Net Papers")
treeview.insert('','3','item4',text="Programming")
# insert more items in child
treeview.insert('item2','end','Algorithm',text="Algorithm")
treeview.insert('item2','end','Data Structure',text="Data Structure")
treeview.insert('item3','end','2018 paper',text='2018 paper')
treeview.insert('item3','end','2019 paper',text='2019 paper')
treeview.insert('item4','end','Python',text='Python')
treeview.insert('item4','end','Java',text='Java')
# placing each child items in parent widget
treeview.move('item2','item1','end')
treeview.move('item3','item1','end')
treeview.move('item4','item1','end')

root.mainloop()

