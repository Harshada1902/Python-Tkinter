import tkinter as tk

def set_gradient_bg(window, color1, color2):
    """Create a gradient background on the Tkinter window"""
    canvas = tk.Canvas(window, width=400, height=500)
    canvas.pack(fill="both", expand=True)

    for i in range(256):
        r1, g1, b1 = window.winfo_rgb(color1)
        r2, g2, b2 = window.winfo_rgb(color2)
        r = int(r1 + (r2 - r1) * i / 255) >> 8
        g = int(g1 + (g2 - g1) * i / 255) >> 8
        b = int(b1 + (b2 - b1) * i / 255) >> 8
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i*2, 400, i*2, fill=color)

    canvas.pack(fill="both", expand=True)
    return canvas
