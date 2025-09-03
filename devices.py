# devices.py

# Dictionary to store device states
devices = {
    "light": False,
    "fan": False,
    "tv": False
}

def toggle_device(device, state):
    """Turn a device on or off."""
    if device in devices:
        devices[device] = state
        return f"{device.capitalize()} turned {'ON' if state else 'OFF'}."
    else:
        return f"Device '{device}' not found."

def movie_mode():
    """Movie mode: turn on TV, turn off light and fan."""
    devices["tv"] = True
    devices["light"] = False
    devices["fan"] = False
    return "Movie mode activated: TV ON, Lights OFF, Fan OFF."

def turn_everything_off():
    """Turn all devices off."""
    for d in devices:
        devices[d] = False
    return "All devices turned OFF."

def get_status():
    """Return the current state of all devices."""
    status = [f"{d.capitalize()}: {'ON' if s else 'OFF'}" for d, s in devices.items()]
    return " | ".join(status)
