# AI Image Caption Generator GUI
# This is a simple GUI application using Tkinter and the BLIP model from Hugging Face Transformers
# to generate captions for uploaded images.

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from transformers import BlipProcessor, BlipForConditionalGeneration
import os  # Added for potential env tweaks

# Optional: Force Tkinter display (uncomment if needed)
# os.environ['DISPLAY'] = ':0'  # For Linux; ignore on Windows

class CaptionGeneratorApp:
    def __init__(self, root):
        print("Initializing app...")  # Debug print
        self.root = root
        self.root.title("AI Image Caption Generator")
        self.root.geometry("600x500")
        
        # Set a beautiful background color (light blue gradient-like)
        self.root.configure(bg='#E0F7FA')  # Light cyan background for a fresh look
        
        # Load the pre-trained BLIP model and processor
        try:
            self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
            self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
            print("Model loaded successfully.")  # Debug print
        except Exception as e:
            messagebox.showerror("Model Load Error", f"Failed to load model: {str(e)}. Check internet connection.")
            return

        # GUI Elements with styling
        # Upload button - Styled with colors and font
        self.upload_btn = tk.Button(root, text="Upload Image", command=self.upload_image, 
                                    bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'), 
                                    relief='raised', bd=3, padx=10, pady=5)
        self.upload_btn.pack(pady=15)

        # Image display label - With a subtle border
        self.image_label = tk.Label(root, bg='#E0F7FA', relief='sunken', bd=2)
        self.image_label.pack(pady=10)

        # Caption display label - Styled for readability
        self.caption_label = tk.Label(root, text="", wraplength=500, font=('Arial', 12, 'italic'), 
                                      bg='#E0F7FA', fg='#333333', anchor='center')
        self.caption_label.pack(pady=10)

        # Generate caption button - Matching style, disabled initially
        self.generate_btn = tk.Button(root, text="Generate Caption", command=self.generate_caption, 
                                      bg='#2196F3', fg='white', font=('Arial', 12, 'bold'), 
                                      relief='raised', bd=3, padx=10, pady=5, state=tk.DISABLED)
        self.generate_btn.pack(pady=15)

        # Store image path
        self.image_path = None
        print("GUI elements created.")  # Debug print

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if self.image_path:
            try:
                img = Image.open(self.image_path)
                img = img.resize((300, 300), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.photo)
                self.generate_btn.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Image Error", f"Failed to load image: {str(e)}")

    def generate_caption(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please upload an image first.")
            return
        try:
            raw_image = Image.open(self.image_path).convert('RGB')
            inputs = self.processor(raw_image, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_length=50)
            caption = self.processor.decode(outputs[0], skip_special_tokens=True)
            self.caption_label.config(text=f"Caption: {caption}")
        except Exception as e:
            messagebox.showerror("Caption Error", f"Failed to generate caption: {str(e)}")

# Run the app
if __name__ == "__main__":
    print("Starting Tkinter app...")  # Debug print
    root = tk.Tk()
    app = CaptionGeneratorApp(root)
    print("Entering mainloop...")  # Debug print
    root.mainloop()