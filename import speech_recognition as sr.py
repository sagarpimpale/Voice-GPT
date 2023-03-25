import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to handle spoken commands
def handle_command(command):
    # Use the ChatGPT model to generate a response
    response = chatGPT.generate_response(command)
    # Convert the response to speech
    engine.say(response)
    engine.runAndWait()

# Define a function to listen for spoken commands
def listen_for_commands():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        # Use the speech recognizer to transcribe the spoken command
        command = r.recognize_google(audio)
        print("Command: " + command)
        # Handle the spoken command
        handle_command(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        print("Error: " + str(e))

# Start listening for spoken commands
while True:
    listen_for_commands()
