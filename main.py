# main.py
import threading
from app import app
from devices import toggle_device, movie_mode, turn_everything_off, get_status
from voice_commands import listen_command, speak

def handle_command(command):
    """Interpret and run commands."""
    if "turn on light" in command:
        response = toggle_device("light", True)
    elif "turn off light" in command:
        response = toggle_device("light", False)
    elif "turn on fan" in command:
        response = toggle_device("fan", True)
    elif "turn off fan" in command:
        response = toggle_device("fan", False)
    elif "turn on tv" in command:
        response = toggle_device("tv", True)
    elif "turn off tv" in command:
        response = toggle_device("tv", False)
    elif "movie mode" in command:
        response = movie_mode()
    elif "turn everything off" in command:
        response = turn_everything_off()
    elif "status" in command:
        response = get_status()
    else:
        response = "Sorry, I didn’t understand that."
    return response

def run_voice_control():
    """Voice recognition loop in a thread."""
    speak("Voice Control Device Switcher is now running with dashboard.")
    print("Say a command (or type if mic fails). Example: 'Turn on light', 'Movie mode', 'Status'")

    while True:
        command = listen_command()
        if command in ["exit", "quit", "stop"]:
            speak("Goodbye! Shutting down voice control.")
            break
        response = handle_command(command)
        print(f"➡️ {response}")
        speak(response)

def run_flask():
    """Run the Flask web dashboard."""
    app.run(debug=False, use_reloader=False)

if __name__ == "__main__":
    # Start Flask in one thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Run Voice Control in main thread
    run_voice_control()
