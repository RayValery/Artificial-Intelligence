import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import pyaudio

def talk(words):
    print (words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
    
talk("Привет! Спроси у меня что-либо")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print ("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

    try:
        zadacha = r.recognize_google(audio).lower()
        print ("Вы сказали: " + zadacha)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadacha = command()

    return zadacha

import pyowm

def Weather(Location):
    owm = pyowm.OWM('840606eb1d42ccb95bf6b2f2f9f5e3ac')
    location = owm.weather_at_place(Location)

    weather = location.get_weather()
    wind = {'wind': weather.get_wind()}
    humidity = {'humidity': weather.get_humidity()}
    temperature = weather.get_temperature('celsius')

    AllWeather = [weather, wind, humidity, temperature]

    print('\n'.join(str(value) for value in AllWeather))


def makeSomething(zadacha):
    if "open website" in zadacha:
        talk("Уже открываю!")
        url = 'https://www.facebook.com/profile.php?id=100017282853915'
        webbrowser.open(url)
    elif "stop" in zadacha:
        talk("Да, конечно. Пока")
        sys.exit()
    elif "name" in zadacha:
        talk("Меня зовут Александра")
    elif "weather" in zadacha:
        talk("Назовите город, в котором вы хотите узнать погоду")
        a = command()
        str(a)
        talk("Назовите страну, в которой находится город")
        b = command()
        str(b)
        с = a + ', ' + b
        print (с)
        talk("Прогноз готов")
        Weather(с)


while True:
    makeSomething(command())
