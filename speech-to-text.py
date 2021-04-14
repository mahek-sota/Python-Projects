import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Begin Recording")
    audio = r.listen(source)

try:
    print(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition can not understand")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition Service;(0)".format(e))