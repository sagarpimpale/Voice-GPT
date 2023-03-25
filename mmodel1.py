import speech_recognition as sr
import pyttsx3
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Initialize the speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to handle spoken commands
def handle_command(command):
    # Generate a response using the ChatGPT model
    input_ids = tokenizer.encode(command, return_tensors="pt")
    response_ids = model.generate(input_ids, max_length=50, num_beams=5)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
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
