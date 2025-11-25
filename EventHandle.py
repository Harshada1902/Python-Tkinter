import tkinter as tk
def on_key_press(event):
    print(f"Key Pressed:{event.keysym}")
def on_left_click(event):
    print(f"Left click at{event.x},{event.y}")
def on_right_click(event):
    print(f"Right click at:{event.x},{event.y}")
def on_mouse_motion(event):
    print(f"Mouse moved to({event.x},{event.y})")

root=tk.Tk()
root.title("Event Handling Example")

root.bind("<KeyPress>",on_key_press)
root.bind("<Button-1>",on_left_click)  #kinter uses <Button-1> for left click
root.bind("<Button-3>",on_right_click)   #<Button-2> for middle click (or scroll wheel), and <Button-3> for right click.
root.bind("<Motion>",on_mouse_motion)
root.mainloop()





