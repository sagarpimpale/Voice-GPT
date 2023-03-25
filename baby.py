import speech_recognition as sr
from google.cloud import texttospeech
import pyaudio
import wave

# Initialize speech recognition and text-to-speech clients
r = sr.Recognizer()
client = texttospeech.TextToSpeechClient()

# Set up voice configuration
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Set up audio configuration
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

# Listen for user input
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Convert speech input to text
try:
    text_input = r.recognize_google(audio)
    print(f"You said: {text_input}")
except sr.UnknownValueError:
    print("Speech recognition could not understand audio")
except sr.RequestError as e:
    print(f"Speech recognition service error: {e}")

# Process the text input and generate a response
response_text = "Hello, how can I assist you?"

# Generate speech from the response text
synthesis_input = texttospeech.SynthesisInput(text=response_text)
response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice,
    audio_config=audio_config
)

# Save audio to file
with open("output.wav", "wb") as out:
    out.write(response.audio_content)

# Play audio response
CHUNK = 1024

with wave.open("output.wav", "rb") as wave_file:
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(wave_file.getsampwidth()),
        channels=wave_file.getnchannels(),
        rate=wave_file.getframerate(),
        output=True
    )
    data = wave_file.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wave_file.readframes(CHUNK)
    stream.stop_stream()
    stream.close()
    p.terminate()

# Delete audio file
os.remove("output.wav")
