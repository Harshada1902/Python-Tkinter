import tkinter as tk
from tkinter import messagebox, ttk

# ---------- Functions ----------
def add_task():
    task = task_entry.get()
    if task.strip() != "":
        listbox.insert(tk.END, "• " + task.strip())
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("✨ Modern To-Do List App ✨")
root.geometry("480x550")
root.resizable(False, False)
root.config(bg="#F8FAFB")

# ---------- Styles ----------
style = ttk.Style()
style.configure("RoundedButton.TButton",
                font=("Poppins", 12, "bold"),
                foreground="white",
                padding=8,
                borderwidth=0)

def make_button(master, text, color, command):
    btn = ttk.Button(master, text=text, command=command, style="RoundedButton.TButton")
    style.map("RoundedButton.TButton",
              background=[("active", color), ("!disabled", color)])
    btn.config(cursor="hand2")
    btn.pack(side=tk.LEFT, padx=8)
    return btn

# ---------- Title ----------
title_frame = tk.Frame(root, bg="#F8FAFB")
title_frame.pack(pady=20)

title_label = tk.Label(title_frame, text="📝 My To-Do List", font=("Poppins", 22, "bold"), bg="#F8FAFB", fg="#2C3E50")
title_label.pack()

# ---------- Entry Box ----------
entry_frame = tk.Frame(root, bg="#F8FAFB")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, font=("Poppins", 14), width=28, relief="flat", bg="#ECF0F1")
task_entry.pack(side=tk.LEFT, ipady=8, padx=10)

add_btn = tk.Button(entry_frame, text="＋", font=("Arial", 16, "bold"), bg="#27AE60", fg="white",
                    activebackground="#2ECC71", activeforeground="white", relief="flat", width=4, command=add_task)
add_btn.pack(side=tk.LEFT)

# ---------- Listbox ----------
list_frame = tk.Frame(root, bg="#F8FAFB")
list_frame.pack(pady=20)

listbox = tk.Listbox(list_frame, font=("Poppins", 14),
                     width=40, height=12, bd=0, bg="#FFFFFF",
                     fg="#2C3E50", selectbackground="#A3E4D7",
                     highlightthickness=2, relief="flat", highlightcolor="#3498DB")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)

# Add scrollbar
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#F8FAFB")
button_frame.pack(pady=20)

delete_btn = tk.Button(button_frame, text="🗑 Delete", font=("Poppins", 12, "bold"),
                       bg="#E74C3C", fg="white", relief="flat", width=10, command=delete_task)
delete_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="🧹 Clear All", font=("Poppins", 12, "bold"),
                      bg="#3498DB", fg="white", relief="flat", width=10, command=clear_all)
clear_btn.grid(row=0, column=1, padx=10)

save_btn = tk.Button(button_frame, text="💾 Save", font=("Poppins", 12, "bold"),
                     bg="#9B59B6", fg="white", relief="flat", width=10, command=save_tasks)
save_btn.grid(row=0, column=2, padx=10)

# ---------- Footer ----------
footer_label = tk.Label(root, text="Made with ❤️ using Tkinter", font=("Poppins", 10), bg="#F8FAFB", fg="#7F8C8D")
footer_label.pack(side=tk.BOTTOM, pady=10)

# ---------- Load tasks on start ----------
load_tasks()

root.mainloop()
