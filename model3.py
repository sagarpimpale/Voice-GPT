import speech_recognition as sr
import pyttsx3
# create a recognizer object
r = sr.Recognizer()


# create a TTS engine instance
engine = pyttsx3.init()

# set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set the first available voice


greetings="Hi...how may i help you? please say something"
print(greetings)
engine.say(greetings)
engine.runAndWait()
print(" I'm listening.....")
# define the audio source
with sr.Microphone() as source:
    
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    text = r.recognize_google(audio)
    print("speech to text: {}".format(text))
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".format(e))
a="hello"

if(text==a):
    print("hello..how are you?")
    engine.say(text+"how are you?")
    engine.runAndWait()
return text
else:
    # convert text to speech
    text="you said:"+text
    print(text)
    engine.say(text)
    engine.runAndWait()
    






