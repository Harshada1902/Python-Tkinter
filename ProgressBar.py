import tkinter as tk
from tkinter import ttk
import time
def start_progress():
    progress.start()
    # Simulate a task that takes time to complete
    for i in range(10):
        time.sleep(0.05)
        progress['value']=i
        # Update the GUI
        root.update_ideletasks()    
    progress.stop()
root=tk.Tk()
root.title("Progressbar example")

# Create progress bar widget
progress=ttk.Progressbar(root,orient='horizontal',length=300,mode="determinate")
progress.pack(pady=20)

# Button to start Progress
start_button=tk.Button(root,text="Start Progress",command=start_progress)
start_button.pack(pady=10)
root.mainloop()