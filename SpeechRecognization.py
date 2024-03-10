# Importing necessary libraries
import pyttsx3  # Library for text-to-speech conversion
import speech_recognition as sr  # Library for speech recognition

# Function to get user's voice input
def get_user_voice(timeout=5):
    recognizer = sr.Recognizer()  # Creating a recognizer object

    with sr.Microphone() as source:
        print(f"Please speak within {timeout} seconds to set your voice...")  # Prompt user to speak
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjusting for ambient noise
        try:
            audio = recognizer.listen(source, timeout=timeout)  # Listen to user's voice input
        except sr.WaitTimeoutError:
            print("Time's up. No voice detected.")  # Handling timeout
            return None

    try:
        print("Recognizing your voice...")  # Indicating voice recognition process
        user_voice = recognizer.recognize_google(audio)  # Recognizing user's voice using Google Speech Recognition
        print(f"Your voice is recognized as: {user_voice}")  # Displaying recognized voice
        return user_voice
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")  # Handling unrecognized voice
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")  # Handling request error

    return None

# Function to set voice based on user's name
def set_voice_by_name(name):
    voices = engine.getProperty('voices')  # Getting available voices
    for voice in voices:
        if name.lower() in voice.name.lower():  # Checking if user's name matches any available voice
            engine.setProperty('voice', voice.id)  # Setting the voice
            return True
    print(f"Voice with name '{name}' not found.")  # Displaying error if user's name is not found
    return False

engine = pyttsx3.init()  # Initializing the text-to-speech engine

# Warm-up the engine to avoid initialization delay during user interaction
engine.say("Initializing voice recognition. Please wait.")
engine.runAndWait()

user_voice = get_user_voice()  # Getting user's voice input

if user_voice:
    if set_voice_by_name(user_voice):  # Setting voice based on user's input
        answer = input("Type what's in your mind, and I can read it for you: ")  # Prompting user to input text
        engine.say(answer)  # Converting input text to speech
        engine.runAndWait()  # Running the text-to-speech engine
