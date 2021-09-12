# Webscraping weather website
# import requests
# api = "087aedbe9b86301f4bfd9806eb780589"
# city = 'afghanistan'
# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
# page = requests.get(url)
# res = page.json()
# print(res)
# if res['cod'] != '404':
#         a = res["weather"][0]
#         condition = a["description"]
#         y = res['main']
#         temp = y["temp"]
#         feel_temp = y['feels_like']
#         humidity = y['humidity']
#         print(temp,feel_temp,condition,humidity)

# Time
# a =str(datetime.now().time())
# if a[:2] > '12':
#         hour = int(a[:2])- 12
#         print(f'it is {hour}:{a[3:5]} pm')
# else:
#         print(f'it is {a[:5]} am')

# open folder
# webbrowser.open("F:\\Movies")

#  show old pics
from random import *
from os import *
num = choice([1,2])
if num ==1:
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
elif num ==2:
    path2 = 'F:\\Photos'
    songs = listdir(path2)
    li = []
    another = []
    for i in songs:
        a = f'F:\\Photos\\{i}'
        li.append(a)
        ass = listdir(a)
        another.append(ass)
    folders = ['.thumbnails', '100_CFV5', 'adi', 'Allen', 'Avinash19 birthday', 'birthday and ghumi', 'Camera', 'Camera MX', 'Camera12', 'Camera2', 'CANON DUMRAON', 'CANON M50', 'captured_media', 'del', 'DELHI', 'DSLRCamera', 'Efectum', 'gautam wedding', 'ghc', 'guddu bhaiya cam', 'NEW YEAR AND STUF', 'PAPU GREAT WED', 'Recived Pics', 'Screenshots', 'Tour Pics', 'Ujwal', 'Vivek college', 'whatsapp2', 'YouCam Perfect', 'YouCam Perfect2']
    index = folders.index(choice(folders))
    startfile(path.join(li[index], another[index][randint(1, len(another[index]) - 1)]))
