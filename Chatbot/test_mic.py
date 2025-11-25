import sounddevice as sd
import numpy as np
import speech_recognition as sr

r = sr.Recognizer()

def record_and_recognize(duration=5, fs=44100):
    print("🎙️ Recording... please speak clearly")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    data = np.squeeze(audio)
    audio_data = sr.AudioData(data.tobytes(), fs, 2)

    try:
        print("🧠 Recognizing...")
        text = r.recognize_google(audio_data)
        print("✅ You said:", text)
    except sr.UnknownValueError:
        print("❌ Could not understand.")
    except sr.RequestError:
        print("⚠️ Internet or service error.")

record_and_recognize()
