import tkinter as tk
from datetime import date

def calculate_age():
    # Get input from user
    d = int(day_entry.get())
    m = int(month_entry.get())
    y = int(year_entry.get())

    today = date.today()
    birth = date(y, m, d)

    # Calculate years
    years = today.year - birth.year
    months = today.month - birth.month
    days = today.day - birth.day

    # Adjust if needed
    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    result_label.config(text=f"Your Age is: {years} Years, {months} Months, {days} Days")

# Create window
win = tk.Tk()
win.title("Age Calculator")
win.geometry("300x300")

# Labels and Entries
tk.Label(win, text="Enter Birth Day:").pack()
day_entry = tk.Entry(win)
day_entry.pack()

tk.Label(win, text="Enter Birth Month:").pack()
month_entry = tk.Entry(win)
month_entry.pack()

tk.Label(win, text="Enter Birth Year:").pack()
year_entry = tk.Entry(win)
year_entry.pack()

# Button
tk.Button(win, text="Calculate Age", command=calculate_age, bg="green", fg="white").pack(pady=10)
# Result
result_label = tk.Label(win, text="", font=("Arial", 12))
result_label.pack(pady=10)

win.mainloop()
