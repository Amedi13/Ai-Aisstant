import pyttsx3

# Initialize the TTS engine once
engine = pyttsx3.init()

def speak(text):
    """
    Converts text to speech and says it out loud.
    """
    print(f"Amadeus: {text}")
    engine.say(text)
    engine.runAndWait()