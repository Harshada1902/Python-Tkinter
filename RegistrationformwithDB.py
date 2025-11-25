import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- Database Connection ----------------
def connect_db():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            gender TEXT NOT NULL,
            country TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Database connected successfully!")

# ---------------- Register User ----------------
def register_user():
    fullname = entry_fullname.get()
    email = entry_email.get()
    gender = gender_var.get()
    country = entry_country.get()
    password = entry_password.get()

    if not (fullname and email and gender and country and password):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user(fullname, email, gender, country, password) VALUES (?, ?, ?, ?, ?)",
            (fullname, email, gender, country, password)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Registration Successful!")
        show_login_window()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists!")

# ---------------- Login User ----------------
def login_user():
    email = login_email.get()
    password = login_password.get()

    if not (email and password):
        messagebox.showerror("Error", "Please fill all fields!")
        return

    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", f"Welcome {result[1]}!")
        login_window.destroy()
        open_dashboard(result[1])
    else:
        messagebox.showerror("Error", "Invalid Email or Password!")

# ---------------- Dashboard ----------------
def open_dashboard(username):
    dash = tk.Tk()
    dash.title("Dashboard")
    dash.geometry("300x200")
    dash.config(bg="cyan")

    tk.Label(dash, text=f"Welcome, {username}!", font=("Arial", 16, "bold"), bg="cyan", fg="#1b5e20").pack(pady=40)
    tk.Button(dash, text="Logout", command=dash.destroy, bg="#1b5e20", fg="white", width=10).pack()
    dash.mainloop()

# ---------------- Registration Window ----------------
def show_register_window():
    global root, entry_fullname, entry_email, gender_var, entry_country, entry_password
    login_window.destroy()

    root = tk.Tk()
    root.title("User Registration")
    root.geometry("400x450")
    root.config(bg="#e3f2fd")

    tk.Label(root, text="Full Name", bg="#e3f2fd").pack(anchor="w", padx=30)
    entry_fullname = tk.Entry(root)
    entry_fullname.pack(fill='x', padx=30, pady=5)

    tk.Label(root, text="Email", bg="#e3f2fd").pack(anchor="w", padx=30)
    entry_email = tk.Entry(root)
    entry_email.pack(fill='x', padx=30, pady=5)

    tk.Label(root, text="Gender", bg="#e3f2fd").pack(anchor="w", padx=30)
    gender_var = tk.StringVar()
    tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#e3f2fd").pack()
    tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#e3f2fd").pack()

    tk.Label(root, text="Country", bg="#e3f2fd").pack(anchor="w", padx=30)
    entry_country = tk.Entry(root)
    entry_country.pack(fill='x', padx=30, pady=5)

    tk.Label(root, text="Password", bg="#e3f2fd").pack(anchor="w", padx=30)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(fill='x', padx=30, pady=5)

    tk.Button(root, text="Register", bg="#1b5e20", fg="white", command=register_user).pack(pady=10)
    tk.Button(root, text="Back to Login", bg="gray", fg="white", command=show_login_window).pack()

    root.mainloop()

# ---------------- Login Window ----------------
def show_login_window():
    global login_window, login_email, login_password
    try:
        root.destroy()
    except:
        pass

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("350x300")
    login_window.config(bg="#f1f8e9")

    tk.Label(login_window, text="Login to Continue", font=("Arial", 18, "bold"), bg="#f1f8e9", fg="#33691e").pack(pady=15)

    tk.Label(login_window, text="Email", bg="#f1f8e9").pack(anchor="w", padx=30)
    login_email = tk.Entry(login_window)
    login_email.pack(fill='x', padx=30, pady=5)

    tk.Label(login_window, text="Password", bg="#f1f8e9").pack(anchor="w", padx=30)
    login_password = tk.Entry(login_window, show="*")
    login_password.pack(fill='x', padx=30, pady=5)

    tk.Button(login_window, text="Login", bg="#33691e", fg="white", command=login_user).pack(pady=10)
    tk.Button(login_window, text="Register", bg="gray", fg="white", command=show_register_window).pack()

    login_window.mainloop()

# ---------------- Run App ----------------
connect_db()
show_login_window()