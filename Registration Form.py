import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    courses = []
    if python_var.get():
        courses.append("Python")
    if cpp_var.get():
        courses.append("C++")
    if java_var.get():
        courses.append("Java")

    message = f"Name: {name}\nEmail: {email}\nGender: {gender}\nCourses: {', '.join(courses)}"
    messagebox.showinfo("Registration Details", message)

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x350")
root.config(bg="lightblue")

tk.Label(root, text="Registration Form", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Label(root, text="Courses").pack()
python_var = tk.BooleanVar()
cpp_var = tk.BooleanVar()
java_var = tk.BooleanVar()
tk.Checkbutton(root, text="Python", variable=python_var).pack()
tk.Checkbutton(root, text="C++", variable=cpp_var).pack()
tk.Checkbutton(root, text="Java", variable=java_var).pack()

tk.Button(root, text="Submit", command=submit,bg="yellow").pack(pady=10)

root.mainloop()