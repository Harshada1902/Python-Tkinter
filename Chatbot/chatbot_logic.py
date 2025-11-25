import pyttsx3
import datetime
import random
import speech_recognition as sr

# Initialize Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    """Speak the given text aloud"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user voice and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError:
        print("Speech recognition service error")
        return ""

def chatbot_reply(text):
    """Return chatbot response for given text"""
    text = text.lower()

    # --- Food-related responses ---
    food_responses = {
        "pizza": "I love pizza too! Especially cheese burst 🍕",
        "burger": "A burger is always a good idea 🍔",
        "food": "I like everything, but you should eat healthy 🥗"
    }

    # --- Jokes ---
    jokes = [
        "Why don’t skeletons fight each other? Because they don’t have the guts! 😂",
        "What do you call fake spaghetti? An impasta! 🍝",
        "I told my computer I needed a break, and it said 'No problem — I’ll go to sleep!' 😴"
    ]

    # --- Weather & Temperature ---
    if "weather" in text:
        return "I'm not connected to live weather now, but it looks sunny and beautiful outside! ☀️"
    if "temperature" in text:
        return "It feels like a pleasant 25°C today! 🌡️"

    # --- Date / Time ---
    if "time" in text:
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"
    if "date" in text:
        return f"Today’s date is {datetime.date.today().strftime('%B %d, %Y')}"

    # --- Likes / Favorites ---
    if "your name" in text:
        return "I’m your friendly AI Chatbot 🤖"
    if "like" in text or "favourite" in text:
        return random.choice(["I like talking with you 😄", "My favorite thing is learning new stuff!", "I love helping humans! ❤️"])

    # --- Novels / Books ---
    if "novel" in text or "book" in text:
        return "I recommend reading 'The Alchemist' by Paulo Coelho — it's inspiring! 📖"

    # --- Tell a joke ---
    if "joke" in text:
        return random.choice(jokes)

    # --- Greetings ---
    greetings = ["hi", "hello", "hey"]
    if any(word in text for word in greetings):
        return random.choice(["Hello there 👋", "Hi! How are you today?", "Hey! Nice to see you!"])

    # --- Default ---
    return random.choice([
        "Hmm, interesting! Tell me more 🤔",
        "That’s cool! What else do you like?",
        "I didn’t quite get that, can you rephrase?",
        "Let’s talk about something fun! 😄"
    ])
