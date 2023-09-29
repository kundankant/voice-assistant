import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def process_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you?")
    elif "how are you" in command:
        speak("I'm just a computer program, but I'm doing well. How can I help you?")
    elif "thank you" in command:
        speak("You're welcome!")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop
while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        process_command(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
