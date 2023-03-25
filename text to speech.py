import pyttsx3

# create a TTS engine instance
engine = pyttsx3.init()

# set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # set the first available voice

# convert text to speech
text = "As I gaze into your eyes, I am lost in a world of pure beauty and wonder. Your smile brightens up my day and your touch sends shivers down my spine. With you by my side, I am complete. I will cherish every moment spent with you and hold you close to my heart. You are my soulmate, my everything, and I vow to love you forever."
engine.say(text)
print(text)
engine.runAndWait()
