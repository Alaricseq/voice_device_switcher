# voice_commands.py
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    """Speak text using pyttsx3."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for a voice command. If mic fails, fallback to text input."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio).lower()
            print(f"✅ Heard: {command}")
            return command
    except Exception as e:
        print(f"(Fallback) Mic issue: {e}")
        return input("⌨️ Enter command: ").lower()
