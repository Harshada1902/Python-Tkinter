from tkinter import *

win = Tk()
win.title("Calculator")
win.configure(bg="lightblue")

# Fixed window size
window_width = 300
window_height = 400

# Get screen dimensions
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate position to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set geometry and make non-resizable
win.geometry(f"{window_width}x{window_height}+{x}+{y}")
win.resizable(False, False)

# Row/column configuration
for i in range(5):
    win.rowconfigure(i, weight=1)
for i in range(4):
    win.columnconfigure(i, weight=1)

# Entry box
box = Entry(win, font=("Arial", 18), bd=5, relief=RIDGE, justify="right")
box.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Functions
def click(n):
    box.insert(END, n)

def clear():
    box.delete(0, END)

def equal():
    ans = eval(box.get())
    box.delete(0, END)
    box.insert(END, ans)

# Normal button style
btn_style = {"font": ("Arial", 14), "bg": "white", "bd": 3}

# Buttons layout
Button(win, text="1", command=lambda: click("1"), **btn_style).grid(row=1, column=0, sticky="nsew", padx=3, pady=3)
Button(win, text="2", command=lambda: click("2"), **btn_style).grid(row=1, column=1, sticky="nsew", padx=3, pady=3)
Button(win, text="3", command=lambda: click("3"), **btn_style).grid(row=1, column=2, sticky="nsew", padx=3, pady=3)
Button(win, text="+", command=lambda: click("+"), **btn_style).grid(row=1, column=3, sticky="nsew", padx=3, pady=3)

Button(win, text="4", command=lambda: click("4"), **btn_style).grid(row=2, column=0, sticky="nsew", padx=3, pady=3)
Button(win, text="5", command=lambda: click("5"), **btn_style).grid(row=2, column=1, sticky="nsew", padx=3, pady=3)
Button(win, text="6", command=lambda: click("6"), **btn_style).grid(row=2, column=2, sticky="nsew", padx=3, pady=3)
Button(win, text="-", command=lambda: click("-"), **btn_style).grid(row=2, column=3, sticky="nsew", padx=3, pady=3)

Button(win, text="7", command=lambda: click("7"), **btn_style).grid(row=3, column=0, sticky="nsew", padx=3, pady=3)
Button(win, text="8", command=lambda: click("8"), **btn_style).grid(row=3, column=1, sticky="nsew", padx=3, pady=3)
Button(win, text="9", command=lambda: click("9"), **btn_style).grid(row=3, column=2, sticky="nsew", padx=3, pady=3)
Button(win, text="*", command=lambda: click("*"), **btn_style).grid(row=3, column=3, sticky="nsew", padx=3, pady=3)

Button(win, text="C", command=clear, font=("Arial",14), bg="red", fg="white", bd=3).grid(row=4, column=0, sticky="nsew", padx=3, pady=3)
Button(win, text="0", command=lambda: click("0"), **btn_style).grid(row=4, column=1, sticky="nsew", padx=3, pady=3)
Button(win, text="=", command=equal, font=("Arial",14), bg="lightgreen", bd=3).grid(row=4, column=2, sticky="nsew", padx=3, pady=3)
Button(win, text="/", command=lambda: click("/"), **btn_style).grid(row=4, column=3, sticky="nsew", padx=3, pady=3)

win.mainloop()
