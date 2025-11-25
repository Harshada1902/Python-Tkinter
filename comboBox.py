import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item=combo_box.get()
    label.config(text="Selected Item:" + selected_item)

root=tk.Tk()
root.title("Combobox Example")

# Create a label
label=tk.Label(root,text="Selected Item:")
label.pack(pady=10)

# Create a Combobox widget
combo_box=ttk.Combobox(root,values=["Option1","Option2","Option3"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Option1")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>",select)
root.mainloop()
