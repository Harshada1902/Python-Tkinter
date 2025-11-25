import tkinter as tk
from tkinter import messagebox
import random
import winsound  # For sound effects

# -----------------------------
# QUIZ DATA
# -----------------------------
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Picasso", "Van Gogh", "Michelangelo"], "answer": "Leonardo da Vinci"},
    {"question": "Which is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": "2"},
    {"question": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "Who discovered gravity?", "options": ["Newton", "Einstein", "Galileo", "Edison"], "answer": "Newton"},
    {"question": "What is H2O commonly known as?", "options": ["Water", "Oxygen", "Hydrogen", "Salt"], "answer": "Water"},
    {"question": "What is 15 + 6?", "options": ["20", "21", "22", "23"], "answer": "21"},
    {"question": "Which continent is India in?", "options": ["Asia", "Europe", "Africa", "Australia"], "answer": "Asia"},
    {"question": "Who was the first man to walk on the Moon?", "options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"], "answer": "Neil Armstrong"},
    {"question": "Which animal is known as the King of the Jungle?", "options": ["Tiger", "Lion", "Elephant", "Cheetah"], "answer": "Lion"},
    {"question": "What is the national fruit of India?", "options": ["Apple", "Banana", "Mango", "Orange"], "answer": "Mango"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Charles Dickens", "Mark Twain", "George Orwell"], "answer": "William Shakespeare"},
    {"question": "What is the largest mammal?", "options": ["Elephant", "Whale", "Giraffe", "Hippo"], "answer": "Whale"},
    {"question": "Which is the fastest land animal?", "options": ["Tiger", "Cheetah", "Leopard", "Lion"], "answer": "Cheetah"},
    {"question": "What is the boiling point of water?", "options": ["100°C", "90°C", "80°C", "120°C"], "answer": "100°C"},
    {"question": "Which planet is closest to the sun?", "options": ["Mercury", "Venus", "Earth", "Mars"], "answer": "Mercury"},
    {"question": "What is the chemical symbol for gold?", "options": ["Ag", "Au", "Fe", "Gd"], "answer": "Au"},
    {"question": "Which bird can mimic human speech?", "options": ["Crow", "Parrot", "Eagle", "Sparrow"], "answer": "Parrot"},
    {"question": "Which color is formed by mixing red and white?", "options": ["Pink", "Purple", "Orange", "Brown"], "answer": "Pink"},
    {"question": "Which festival is known as the festival of lights?", "options": ["Holi", "Diwali", "Christmas", "Eid"], "answer": "Diwali"},
    {"question": "Which device is used to measure temperature?", "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], "answer": "Thermometer"},
    {"question": "What is the national currency of Japan?", "options": ["Yuan", "Yen", "Dollar", "Won"], "answer": "Yen"},
    {"question": "Which gas is essential for breathing?", "options": ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "answer": "Oxygen"},
    {"question": "How many days are there in a leap year?", "options": ["364", "365", "366", "367"], "answer": "366"},
    {"question": "Which part of the plant conducts photosynthesis?", "options": ["Stem", "Leaf", "Root", "Flower"], "answer": "Leaf"},
    {"question": "Which organ pumps blood in the human body?", "options": ["Liver", "Brain", "Heart", "Kidney"], "answer": "Heart"},
    {"question": "Which animal gives us wool?", "options": ["Cow", "Sheep", "Goat", "Horse"], "answer": "Sheep"},
    {"question": "Which shape has three sides?", "options": ["Square", "Triangle", "Rectangle", "Pentagon"], "answer": "Triangle"},
]

random.shuffle(quiz_data)

# -----------------------------
# MAIN APP CLASS
# -----------------------------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Quiz Master 🧠")
        self.root.geometry("600x420")
        self.root.config(bg="#f2f2f2")

        self.username = ""
        self.timer_job = None
        self.question_index = 0
        self.score = 0
        self.time_left = 10

        self.start_screen()

    # ---------------- START SCREEN ----------------
    def start_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Welcome to Smart Quiz Master 🧠", font=("Comic Sans MS", 20, "bold"), bg="#f2f2f2", fg="#333").pack(pady=20)
        tk.Label(self.root, text="Enter your name:", font=("Arial", 14), bg="#f2f2f2").pack(pady=10)
        self.name_entry = tk.Entry(self.root, font=("Arial", 14), width=25)
        self.name_entry.pack(pady=5)
        tk.Button(self.root, text="Start Quiz ➜", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.start_quiz).pack(pady=20)

    # ---------------- QUIZ SCREEN ----------------
    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name!")
            return
        self.username = name
        self.create_quiz_widgets()
        self.load_question()

    def create_quiz_widgets(self):
        self.clear_window()
        self.title_label = tk.Label(self.root, text=f"Player: {self.username}", font=("Comic Sans MS", 16, "bold"), fg="#333", bg="#f2f2f2")
        self.title_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="Time: 10s", font=("Arial", 14, "bold"), fg="red", bg="#f2f2f2")
        self.timer_label.pack(pady=5)

        self.question_label = tk.Label(self.root, text="", wraplength=500, font=("Arial", 16), bg="#f2f2f2", fg="#333")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 14), width=30, bg="#e0e0e0", relief="raised", command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.next_button = tk.Button(self.root, text="Next ➜", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.next_question)
        self.next_button.pack(pady=15)

    # ---------------- LOAD QUESTION ----------------
    def load_question(self):
        if self.question_index < len(quiz_data):
            self.time_left = 10
            self.timer_label.config(text=f"Time: {self.time_left}s")
            q = quiz_data[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}. {q['question']}")
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=option, state="normal", bg="#e0e0e0", fg="black")

            # Cancel previous timer if running
            if self.timer_job:
                self.root.after_cancel(self.timer_job)
            self.update_timer()
        else:
            self.end_quiz()

    # ---------------- TIMER ----------------
    def update_timer(self):
        self.timer_label.config(text=f"Time: {self.time_left}s")
        if self.time_left > 0:
            winsound.Beep(1000, 100)  # tick sound
            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's Up!", "You ran out of time for this question!")
            self.next_question()

    # ---------------- CHECK ANSWER ----------------
    def check_answer(self, i):
        selected = self.option_buttons[i].cget("text")
        correct = quiz_data[self.question_index]["answer"]

        if self.timer_job:
            self.root.after_cancel(self.timer_job)

        if selected == correct:
            self.score += 1
            winsound.Beep(1500, 200)  # correct sound
            self.option_buttons[i].config(bg="#4CAF50", fg="white")
        else:
            winsound.Beep(600, 200)  # wrong sound
            self.option_buttons[i].config(bg="#f44336", fg="white")

        for btn in self.option_buttons:
            btn.config(state="disabled")

    # ---------------- NEXT QUESTION ----------------
    def next_question(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
        self.question_index += 1
        self.load_question()

    # ---------------- END QUIZ ----------------
    def end_quiz(self):
        self.clear_window()
        score_percent = (self.score / len(quiz_data)) * 100
        result_text = f"🎉 Quiz Completed, {self.username}!\n\nYour Score: {self.score}/{len(quiz_data)}\nPercentage: {score_percent:.2f}%"
        tk.Label(self.root, text=result_text, font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333").pack(pady=50)
        tk.Button(self.root, text="Exit", font=("Arial", 14, "bold"), bg="#f44336", fg="white", command=self.root.destroy).pack(pady=20)

    # ---------------- UTILITY ----------------
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# -----------------------------s
# RUN APP
# -----------------------------
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
