import speech_recognition as sr

r = sr.Recognizer() 

with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)

try:
    text = r.recognize_whisper(audio)
    print("Result:", text)
except Exception as e:
    print("Translation failed", e)