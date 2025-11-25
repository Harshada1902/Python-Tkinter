import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import chatbot_reply, speak, listen
from ui_utils import set_gradient_bg
import threading
import sys

# Fix emoji output issue
sys.stdout.reconfigure(encoding='utf-8')

# --- Main Chatbot App ---
root = tk.Tk()
root.title("AI Chatbot Assistant 🤖")
root.geometry("420x600")
root.resizable(False, False)

canvas = set_gradient_bg(root, "#89f7fe", "#66a6ff")

# --- Chat display ---
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#f4f6f7", fg="#2c3e50", padx=10, pady=10)
chat_box.place(x=10, y=20, width=400, height=450)
chat_box.config(state='disabled')

# --- User input ---
entry = tk.Entry(root, font=("Arial", 13))
entry.place(x=10, y=490, width=280, height=40)

def insert_message(sender, message):
    chat_box.config(state='normal')
    chat_box.insert(tk.END, f"{sender}: {message}\n")
    chat_box.config(state='disabled')
    chat_box.see(tk.END)

def handle_user_message():
    text = entry.get().strip()
    if text:
        insert_message("You", text)
        entry.delete(0, tk.END)
        reply = chatbot_reply(text)
        insert_message("Bot", reply)
        speak(reply)

def handle_voice():
    def listen_and_reply():
        text = listen()
        if text:
            insert_message("You (voice)", text)
            reply = chatbot_reply(text)
            insert_message("Bot", reply)
            speak(reply)
        else:
            insert_message("Bot", "I couldn’t hear you properly. Please try again 🎙️")
    threading.Thread(target=listen_and_reply).start()

send_btn = tk.Button(root, text="Send 💬", command=handle_user_message, font=("Arial", 11, "bold"), bg="#2ecc71", fg="white")
send_btn.place(x=300, y=490, width=90, height=40)

mic_btn = tk.Button(root, text="🎤 Speak", command=handle_voice, font=("Arial", 11, "bold"), bg="#3498db", fg="white")
mic_btn.place(x=10, y=540, width=380, height=40)

insert_message("Bot", "Hello! I’m your AI Chatbot. You can type or talk to me. 😊")

root.mainloop()
