import tkinter as tk
from datetime import date

def calculate_age():
    try:
        # Get user inputs
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())

        today = date.today()
        birth_date = date(birth_year, birth_month, birth_day)

        # Calculate difference in years, months, and days
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1
            prev_month = (today.month - 1) or 12
            if prev_month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31
            elif prev_month in [4, 6, 9, 11]:
                days += 30
            else:
                days += 28

        if months < 0:
            years -= 1
            months += 12

        result_label.config(
            text=f"🎂 Your Age is:\n{years} Years, {months} Months, and {days} Days"
        )

    except ValueError:
        result_label.config(text="⚠️ Please enter valid numbers!")

# Create window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x350")
root.config(bg="#d0f0c0")

# Title
tk.Label(
    root, text="🧮 Age Calculator", font=("Arial", 18, "bold"),
    bg="#4CAF50", fg="white", pady=10
).pack(fill=tk.X)

# Frame for inputs
frame = tk.Frame(root, bg="#d0f0c0")
frame.pack(pady=20)

# Input fields
tk.Label(frame, text="Enter Birth Day:", bg="#d0f0c0", font=("Arial", 12)).grid(row=0, column=0, pady=5, sticky="e")
day_entry = tk.Entry(frame, width=10)
day_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Enter Birth Month:", bg="#d0f0c0", font=("Arial", 12)).grid(row=1, column=0, pady=5, sticky="e")
month_entry = tk.Entry(frame, width=10)
month_entry.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Enter Birth Year:", bg="#d0f0c0", font=("Arial", 12)).grid(row=2, column=0, pady=5, sticky="e")
year_entry = tk.Entry(frame, width=10)
year_entry.grid(row=2, column=1, pady=5)

# Button
tk.Button(
    root, text="Calculate Age", command=calculate_age,
    bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
    padx=10, pady=5
).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", bg="#d0f0c0", font=("Arial", 13, "bold"), justify="center")
result_label.pack(pady=15)

# Footer
tk.Label(root, text="Developed by Harshada 💻", bg="#d0f0c0", font=("Arial", 9, "italic")).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
