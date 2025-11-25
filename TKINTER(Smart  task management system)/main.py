import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import ttkbootstrap as tb  # Modern UI themes
import sqlite3
import bcrypt  # Password hashing
import matplotlib  # Import matplotlib first
matplotlib.use('TkAgg')  # Set backend BEFORE importing pyplot
import matplotlib.pyplot as plt  # Now import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import re  # For search (if needed later)

# Database setup
def setup_database():
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium',
            status TEXT CHECK(status IN ('Pending', 'Completed')) DEFAULT 'Pending',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Task Manager")
        self.root.geometry("1000x700")
        self.center_window(self.root, 1000, 700)  # Center the main window
        self.style = tb.Style(theme="cosmo")  # Start with light theme
        self.current_user = None
        self.show_login_screen()

    def center_window(self, window, width, height):
        # Center any window on the screen
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def show_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)
        
        tb.Label(frame, text="Login", font=("Arial", 24)).pack(pady=10)
        tb.Label(frame, text="Username:").pack()
        self.username_entry = tb.Entry(frame)
        self.username_entry.pack(pady=5)
        tb.Label(frame, text="Password:").pack()
        self.password_entry = tb.Entry(frame, show="*")
        self.password_entry.pack(pady=5)
        
        tb.Button(frame, text="Login", command=self.login, bootstyle="success").pack(pady=10)
        tb.Button(frame, text="Register", command=self.show_register_screen, bootstyle="info").pack()
        tb.Button(frame, text="Toggle Dark Mode", command=self.toggle_theme, bootstyle="secondary").pack(pady=10)

    def toggle_theme(self):
        current = self.style.theme.name
        self.style.theme_use("darkly" if current == "cosmo" else "cosmo")

    def show_register_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        frame = tb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill=tk.BOTH)
        
        tb.Label(frame, text="Register", font=("Arial", 24)).pack(pady=10)
        tb.Label(frame, text="Username:").pack()
        self.reg_username = tb.Entry(frame)
        self.reg_username.pack(pady=5)
        tb.Label(frame, text="Password:").pack()
        self.reg_password = tb.Entry(frame, show="*")
        self.reg_password.pack(pady=5)
        
        tb.Button(frame, text="Register", command=self.register, bootstyle="success").pack(pady=10)
        tb.Button(frame, text="Back to Login", command=self.show_login_screen, bootstyle="secondary").pack()

    def register(self):
        username = self.reg_username.get().strip()
        password = self.reg_password.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful")
            self.show_login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
        finally:
            conn.close()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, password_hash, role FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            
            if user and bcrypt.checkpw(password.encode('utf-8'), user[1]):
                self.current_user = {'id': user[0], 'username': username, 'role': user[2]}
                self.show_main_screen()
            else:
                messagebox.showerror("Error", "Invalid credentials")
        except Exception as e:
            messagebox.showerror("Error", f"Login failed: {str(e)}")
        finally:
            conn.close()

    def show_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        menu_frame = tb.Frame(self.root)
        menu_frame.pack(fill=tk.X, pady=10)
        tb.Button(menu_frame, text="Add Task", command=self.add_task_window, bootstyle="success").pack(side=tk.LEFT, padx=5)
        tb.Button(menu_frame, text="Analytics", command=self.show_analytics, bootstyle="info").pack(side=tk.LEFT, padx=5)
        tb.Button(menu_frame, text="Logout", command=self.logout, bootstyle="danger").pack(side=tk.RIGHT, padx=5)
        
        filter_frame = tb.Frame(self.root)
        filter_frame.pack(fill=tk.X, pady=5)
        tb.Label(filter_frame, text="Search:").pack(side=tk.LEFT)
        self.search_entry = tb.Entry(filter_frame)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tb.Button(filter_frame, text="Search", command=self.search_tasks, bootstyle="primary").pack(side=tk.LEFT)
        tb.Label(filter_frame, text="Filter Priority:").pack(side=tk.LEFT, padx=10)
        self.priority_filter = tb.Combobox(filter_frame, values=["All", "Low", "Medium", "High"])
        self.priority_filter.set("All")
        self.priority_filter.pack(side=tk.LEFT)
        tb.Button(filter_frame, text="Apply Filter", command=lambda: self.load_tasks(priority_filter=self.priority_filter.get()), bootstyle="secondary").pack(side=tk.LEFT, padx=5)
        
        self.task_tree = ttk.Treeview(self.root, columns=("S.No", "Title", "Due Date", "Priority", "Status"), show="headings")
        self.task_tree.heading("S.No", text="S.No")
        self.task_tree.heading("Title", text="Title")
        self.task_tree.heading("Due Date", text="Due Date")
        self.task_tree.heading("Priority", text="Priority")
        self.task_tree.heading("Status", text="Status")
        self.task_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.task_tree.bind("<Double-1>", self.edit_task)
        
        # Add delete button and mark as completed button
        delete_frame = tb.Frame(self.root)
        delete_frame.pack(fill=tk.X, pady=5)
        tb.Button(delete_frame, text="Delete Selected Task", command=self.delete_task, bootstyle="danger").pack(side=tk.LEFT, padx=10)
        tb.Button(delete_frame, text="Mark as Completed", command=self.mark_completed, bootstyle="success").pack(side=tk.LEFT, padx=10)
        
        self.load_tasks()

    def load_tasks(self, search_query="", priority_filter="All"):
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)
        
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            query = "SELECT id, title, due_date, priority, status FROM tasks WHERE user_id = ?"
            params = [self.current_user['id']]
            
            if search_query:
                query += " AND (title LIKE ? OR description LIKE ?)"
                params.extend([f"%{search_query}%", f"%{search_query}%"])
            if priority_filter != "All":
                query += " AND priority = ?"
                params.append(priority_filter)
            
            # Sort by priority (High first, then Medium, Low) and then by due_date ascending
            query += " ORDER BY CASE priority WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 WHEN 'Low' THEN 3 END, due_date ASC"
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            counter = 1
            for row in rows:
                self.task_tree.insert("", tk.END, values=(counter, row[1], row[2], row[3], row[4]), tags=(row[0],))
                counter += 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
        finally:
            conn.close()

    def search_tasks(self):
        query = self.search_entry.get().strip()
        priority_filter = self.priority_filter.get()
        self.load_tasks(search_query=query, priority_filter=priority_filter)

    def add_task_window(self, task_id=None, title="", desc="", due_date="", priority="Medium"):
        self.task_window = tk.Toplevel(self.root)
        self.task_window.title("Add/Edit Task")
        self.task_window.geometry("400x450")  # Increased height to 450 for better button visibility
        self.center_window(self.task_window, 400, 450)  # Center the popup
        self.task_window.transient(self.root)  # Make it modal
        self.task_window.grab_set()  # Disable main window interaction
        self.task_window.resizable(False, False)  # Prevent resizing
        
        tb.Label(self.task_window, text="Title:").pack(pady=5)
        title_entry = tb.Entry(self.task_window)
        title_entry.insert(0, title)
        title_entry.pack(pady=5)
        
        tb.Label(self.task_window, text="Description:").pack(pady=5)
        desc_entry = tk.Text(self.task_window, height=3)
        desc_entry.insert(tk.END, desc)
        desc_entry.pack(pady=5)
        
        tb.Label(self.task_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
        due_entry = tb.Entry(self.task_window)
        due_entry.insert(0, due_date)
        due_entry.pack(pady=5)
        
        tb.Label(self.task_window, text="Priority:").pack(pady=5)
        priority_combo = tb.Combobox(self.task_window, values=["Low", "Medium", "High"])
        priority_combo.set(priority)
        priority_combo.pack(pady=5)
        
        # Button frame for better layout - packed at the bottom with more padding
        button_frame = tb.Frame(self.task_window)
        button_frame.pack(side=tk.BOTTOM, pady=20)  # Pack at bottom with extra padding
        tb.Button(button_frame, text="Save", command=lambda: self.save_task(task_id, title_entry.get().strip(), desc_entry.get("1.0", tk.END).strip(), due_entry.get().strip(), priority_combo.get()), bootstyle="success").pack(side=tk.LEFT, padx=10)
        tb.Button(button_frame, text="Cancel", command=self.task_window.destroy, bootstyle="secondary").pack(side=tk.LEFT, padx=10)

    def save_task(self, task_id, title, desc, due_date, priority):
        if not title:
            messagebox.showerror("Error", "Title is required")
            return
        
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            if task_id:
                cursor.execute("UPDATE tasks SET title=?, description=?, due_date=?, priority=? WHERE id=? AND user_id=?", (title, desc, due_date, priority, task_id, self.current_user['id']))
            else:
                cursor.execute("INSERT INTO tasks (user_id, title, description, due_date, priority) VALUES (?, ?, ?, ?, ?)", (self.current_user['id'], title, desc, due_date, priority))
            conn.commit()
            self.task_window.destroy()
            self.load_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save task: {str(e)}")
        finally:
            conn.close()

    def edit_task(self, event):
        selected = self.task_tree.selection()
        if not selected:
            return
        
        task_id = self.task_tree.item(selected, 'tags')[0]
        
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            cursor.execute("SELECT title, description, due_date, priority FROM tasks WHERE id=? AND user_id=?", (task_id, self.current_user['id']))
            task = cursor.fetchone()
            if task:
                self.add_task_window(task_id=task_id, title=task[0], desc=task[1] or "", due_date=task[2] or "", priority=task[3])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to edit task: {str(e)}")
        finally:
            conn.close()

    def delete_task(self):
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to delete")
            return
        
        if messagebox.askyesno("Confirm", "Delete this task?"):
            task_id = self.task_tree.item(selected, 'tags')[0]
            try:
                conn = sqlite3.connect('task_manager.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM tasks WHERE id=? AND user_id=?", (task_id, self.current_user['id']))
                conn.commit()
                self.load_tasks()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete task: {str(e)}")
            finally:
                conn.close()

    def mark_completed(self):
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to mark as completed")
            return
        
        task_id = self.task_tree.item(selected, 'tags')[0]
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status='Completed' WHERE id=? AND user_id=?", (task_id, self.current_user['id']))
            conn.commit()
            self.load_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to mark task as completed: {str(e)}")
        finally:
            conn.close()

    def logout(self):
        self.current_user = None
        self.show_login_screen()

    def show_analytics(self):
        analytics_win = tk.Toplevel(self.root)
        analytics_win.title("Task Analytics")
        analytics_win.geometry("600x400")
        self.center_window(analytics_win, 600, 400)  # Center the popup
        analytics_win.transient(self.root)  # Make it modal
        analytics_win.grab_set()  # Disable main window interaction
        analytics_win.resizable(False, False)  # Prevent resizing
        
        try:
            conn = sqlite3.connect('task_manager.db')
            cursor = conn.cursor()
            cursor.execute("SELECT priority, COUNT(*) FROM tasks WHERE user_id=? GROUP BY priority", (self.current_user['id'],))
            priority_data = cursor.fetchall()
            cursor.execute("SELECT status, COUNT(*) FROM tasks WHERE user_id=? GROUP BY status", (self.current_user['id'],))
            status_data = cursor.fetchall()
            conn.close()
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
            
            if priority_data:
                priorities, counts = zip(*priority_data)
                ax1.bar(priorities, counts, color='skyblue')
                ax1.set_title("Tasks by Priority")
            else:
                ax1.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax1.transAxes)
            
            if status_data:
                statuses, counts = zip(*status_data)
                ax2.bar(statuses, counts, color='lightgreen')
                ax2.set_title("Tasks by Status")
            else:
                ax2.text(0.5, 0.5, "No data", ha='center', va='center', transform=ax2.transAxes)
            
            # Embed the plot in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=analytics_win)
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            canvas.draw()  # Ensure the plot renders
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load analytics: {str(e)}")

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
