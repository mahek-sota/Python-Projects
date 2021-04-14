import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current Time is ' + time)

    elif 'who the heck is ' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'will you go on a date with me' in command:
        talk('sorry, i have a headache')
    
    elif 'are you single' in command:
        talk('sorry, i am already in a relationship with your wifi')
    
    elif 'jokes' in command:
        talk(pyjokes.get_joke())

    elif 'thank you' in command:
        talk('You are welcome')
        
    else:
        talk('Please say the command again')

while True:
    run_alexa()
