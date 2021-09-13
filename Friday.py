import time
from datetime import datetime
from os import listdir, startfile, path
from random import randint, choice
from sys import exit
from webbrowser import open
import pygame
import pyttsx3
import speech_recognition as sr
import wikipedia
import requests

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
        speak('What is so urgent now.10 to 12 is my sleeping time')
        speak('friday here. what do you need bitch')


def intro():
    print('Hello!')
    speak('Friday here. how may i help you ')


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

        if 'die' in query.lower():
            return query

        elif 'hello' in query.lower() or 'hi friday' in query.lower() or "what's up" in query.lower():
            return 'oo'

        elif 'how are you' in query.lower():
            speak('i am feeling really awesome thanks for asking')

        else:
            print(f"User said: {query}\n")
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

    if active:
        if run_once:
            greeting()
            run_once = False

        # different ways to say hi
        hii = choice(
            ['hi', 'howdy', 'welcome', 'bonjour', 'buenas noches', 'buenos dias', "hi-ya", "how are you", "howdy-do",
             "shalom", "what's happening", "what's up"])

        # get what user said to a string
        result = takeCommand().lower()

        # All Logic Station
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

        if 'google' in result:
            try:
                result = result.replace('google', '')
                open('https://google.com/search?q=%s' % result)
                bye()
            except:
                speak(f'sorry google is having problem with searching {result}')

        if 'weather' in result or 'temperature' in result:
            if 'weather' in result:
                result = result.replace('weather of ', '')
            elif 'temperature' in result:
                result = result.replace('temperature in ', '')
            api = "08edbe9b86301f4bfd9806eb780589"
            city = result
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
            page = requests.get(url)
            res = page.json()
            if res['cod'] != '404':
                a = res["weather"][0]
                y = res['main']
                condition = a["description"]
                temp = y["temp"]
                feel_temp = y['feels_like']
                humidity = y['humidity']
                print(f'Temperature : {temp}  Real Feel : {feel_temp}  humidity : {humidity}%  {condition}')
                speak(
                    f'the temperature is {int(temp)}degree celcius but feels like {int(feel_temp)} humidity is {humidity} percent')
                speak(f'it is {condition}')

        if 'time' in result:
            a = str(datetime.now().time())
            if a[:2] > '12':
                hour = int(a[:2]) - 12
                speak(f'it is {hour}:{a[3:5]} pm')
            else:
                speak(f'it is {a[:5]} am')

        if 'open chrome' in result:
            open('https://www.google.com')
            bye()

        if 'open movies folder' in result:
            open("F:\\Movies")
            bye()

        if 'open code projects' in result:
            open("C:\\Users\\ACE\\PycharmProjects")
            bye()

        if 'open downloads' in result:
            open("C:\\Users\\ACE\\Downloads")
            bye()

        if 'oo' in result: speak(f'{hii} friend how are you!')

        if 'i love you' in result or 'love you' in result: speak('love u too... muah')

        if 'open serial' in result:
            open('https://www.zee5.com/tvshows/details/kumkum-bhagya/0-6-127/latest')
            bye()

        if 'learn python' in result:
            open('https://www.youtube.com/results?search_query=python+projects')
            bye()

        if 'play anime songs' in result:
            music = 'C:\\Users\\ACE\\Downloads\\Video'
            songs = listdir(music)
            startfile(path.join(music, songs[randint(1, len(songs) - 1)]))
            bye()

        if 'play songs' in result:
            open("https://music.youtube.com/playlist?list=LM")
            bye()

        if 'show me old pics' in result:
            num = choice([1, 2])
            if num == 1:
                path1 = 'G:\\Photos'
                songs = listdir(path1)
                li = []
                another = []
                for i in songs:
                    a = f'G:\\Photos\\{i}'
                    li.append(a)
                    ass = listdir(a)
                    another.append(ass)
                folders = ['100CANON', 'CANNON GAON', 'Canon EOS M50', 'dumraon', 'NArgarh', 'New folder1']
                index = folders.index(choice(folders))
                startfile(path.join(li[index], another[index][randint(1, len(another[index]) - 1)]))
            elif num == 2:
                path2 = 'F:\\Photos'
                songs = listdir(path2)
                li = []
                another = []
                for i in songs:
                    a = f'F:\\Photos\\{i}'
                    li.append(a)
                    ass = listdir(a)
                    another.append(ass)
                folders = ['.thumbnails', '100_CFV5', 'adi', 'Allen', 'Avinash19 birthday', 'birthday and ghumi',
                           'Camera', 'Camera MX', 'Camera12', 'Camera2', 'CANON DUMRAON', 'CANON M50', 'captured_media',
                           'del', 'DELHI', 'DSLRCamera', 'Efectum', 'gautam wedding', 'ghc', 'guddu bhaiya cam',
                           'NEW YEAR AND STUF', 'PAPU GREAT WED', 'Recived Pics', 'Screenshots', 'Tour Pics', 'Ujwal',
                           'Vivek college', 'whatsapp2', 'YouCam Perfect', 'YouCam Perfect2']
                index = folders.index(choice(folders))
                startfile(path.join(li[index], another[index][randint(1, len(another[index]) - 1)]))
            bye()

        if 'open calculator' in result:
            open("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Calculator.lnk")
            bye()

        if result[0].isnumeric():
            if 'divided by' in result:
                result = result.replace('divided by', '/')
            if 'into' in result:
                result = result.replace('into', '*')
            try:
                print(eval(result))
                speak(eval(result))
            except:
                speak("couldn't do the calculation. Try saying open calculator")

        if close == 3:
            speak('ok dont speak then go to hell ')
            exit()

        if 'open codechef' in result:
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
            inpu = input('Press Enter to Activate or 1 for Commands : ')
            if '1' in inpu:
                print('''
1.Say anything followed by Wikipedia.
2.Say anything followed by google for google search.
3.Ask weather of or temperature in any city in world.
4.Say play songs                
5.Just say the calculations 
6.Open Codechef
7.Open Youtube
8.Open serial
9.Hi Hello Stuff
10.Open Folders like 'code projects','open movies folder','downloads'
10.And i love you
                ''')
                time.sleep(4)
            if '' in inpu:
               active = True
               space_start = True
