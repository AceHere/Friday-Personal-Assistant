from datetime import datetime
from os import listdir, startfile, path
from random import randint
from sys import exit
from webbrowser import open

import pygame
import pyttsx3
import speech_recognition as sr
import wikipedia

close = 0
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

# initialize pygame
pygame.mixer.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
        intro()
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon sir")
        intro()
    elif hour >= 17 and hour <= 22:
        speak("Good Evening sir")
        intro()
    else:
        speak('What is so urgent now. i was sleeping')
        speak('i am friday. what do you need bitch')


def intro():
    speak('I am Friday. how may i help you ')


def takeCommand():
    # It takes microphone input from the user and returns string output
    global close
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pygame.mixer.music.load('listen.mp3')
        pygame.mixer.music.play()
        print("Listening...")
        r.pause_threshold = 0.9
        r.energy_threshold = 800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        if 'die here' in query.lower():
            return query
        else:
            print(f"User said: {query}\n")
            speak(query)
            close = 0

    except Exception as e:
        if 'connection failed' in str(e):
            print("The Internet seems to be Not Working")
            speak("Turn on your internet ")
        else:
            print("What was that...")
            speak("speak again bitch")
            close += 1
        return "None"
    return query


def bye():
    global active
    speak('Sure. Bye!')
    active = False


space_start = True
run_once = True
active = False
while True:
    if __name__ == '__main__':

        if active:
            if run_once:
                greeting()
                run_once = False

            # get what user said to a string
            result = takeCommand().lower()
            if 'wikipedia' in result:
                try:
                    print('Searching Wikipedia')
                    result = result.replace('wikipedia', '')
                    print(result)
                    print(wikipedia.summary(result, sentences=2))
                    speak(wikipedia.summary(result, sentences=2))
                except:
                    speak(f'Sorry Nothing like {result} was found')

            if 'open youtube' in result:
                open('https://www.youtube.com')
                bye()

            if 'open chrome' in result:
                open('https://www.google.com')
                bye()

            if 'open serial' in result:
                open('https://www.zee5.com/tvshows/details/kumkum-bhagya/0-6-127/latest')
                bye()

            if 'learn python' in result:
                open('https://www.youtube.com/results?search_query=python+projects')
                bye()

            if 'play' in result:
                music = 'C:\\Users\\ACE\\Downloads\\Video'
                songs = listdir(music)
                startfile(path.join(music, songs[randint(1, len(songs) - 1)]))
                bye()

            if close == 3:
                speak('ok dont speak then go to hell ')
                exit()

            if 'codechef' in result:
                open('https://www.codechef.com/problems/easy/')
                bye()

            if 'bye' in result:
                bye()
                exit()

            if 'die' in result:
                speak('as you wish sir')
                pygame.mixer.music.load("hit.mp3")
                pygame.mixer.music.play()
                pygame.time.delay(3000)
                exit()

        else:
            if space_start:
                space_start = False
                print('Press Enter to Activate')
                inpu = input()
                if '' in inpu:
                    active = True
                    space_start = True
