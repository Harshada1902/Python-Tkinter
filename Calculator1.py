import tkinter as tk
from tkinter import messagebox

# Function to update expression in the entry box
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate the expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear entry field
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x420")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=('Arial', 20), borderwidth=5, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, padx=10, sticky="nsew")

# Configure grid weights for even button spacing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, font=('Arial', 18), bg="#4CAF50", fg="white",
                  command=calculate).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    else:
        tk.Button(root, text=text, font=('Arial', 18),
                  command=lambda t=text: press(t)).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
tk.Button(root, text='C', font=('Arial', 18), bg="#f44336", fg="white",
          command=clear).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

root.mainloop()