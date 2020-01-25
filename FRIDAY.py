from tkinter import *

import cv2
import pyttsx3  # pip install pyttsx3
from PIL import ImageTk,Image
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random
import requests
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import roman
import wmi  # pip install wmi
import json
from PIL import Image

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id','password')
    server.sendmail('email.id', to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        var.set("Good morning")
        window.update()
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        var.set("Good Afternoon ")
        window.update()
        speak("Good Afternoon!")

    else:
        var.set("Good Evening ")
        window.update()
        speak("Good Evening!")

    speak("insilising friday...........")
    speak(" I am friday Sir ......")
    speak("How may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Good Evening ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        window.update()

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir I wish you a cherrful day ahead")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir I wish you  a cherrful day ahead")
            break

        # Logic for executing tasks based on query
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            var.set(results)
            window.update()
            speak(results)

        # WEB FUNCTIONALITY

        # SEARCH IN GOOGLE

        elif 'search' in query:
            var.set('searching....')
            com = takeCommand()
            window.update()
            speak("what do you want to search sir..")

            webbrowser.open('https://google.com/search?q=' + ''.join(com))


        # SEARCHING CHANNELS ON YOUTUBE

        elif 'channel' in query:
            var.set('opening Youtube Channel..')
            com = takeCommand()
            window.update()
            speak("which youtube channel do you want to search sir..")

            webbrowser.open('https://youtube.com/search?q=' + ''.join(com))



        # web functins

        elif 'youtube' in query:
            var.set('Opening Youtube')
            window.update()
            speak('opening ....Sir')
            webbrowser.open("www.youtube.com/results?search_query=")

        elif 'google' in query:
            var.set('Opening Google')
            window.update()
            speak('opening ...Sir')
            webbrowser.open("www.google.com")


        elif 'instagram' in query:
            var.set('Opening Instagram')
            window.update()
            speak('opening instagram..Sir')
            webbrowser.open("www.instagram.com")

        elif 'facebook' in query:
            var.set('opening Facebook')
            window.update()
            speak('opening facebook .. Sir')
            webbrowser.open('wwww.facebook.com')

        elif 'twitter' in query:
            var.set('opening twitter')
            window.update()
            speak('opening twitter..Sir')
            webbrowser.open('www.twitter.com')

        elif 'github' in query:
            var.set('opening Github')
            window.update()
            speak('opening github ..Sir')
            webbrowser.open('www.github.com')

        elif 'gmail' in query:
            var.set('opening Gmail')
            window.update()
            speak('opening gmail..Sir')
            webbrowser.open("www.gmail.com")

        elif 'soundcloud' in query:
            var.set('opening Soundcloud')
            window.update()
            speak('opening soundcloud..Sir')
            webbrowser.open("www.soundcloud.com")

        elif 'instructables' in query:
            var.set('opening Instructables')
            window.update()
            speak('opening instructibles..Sir')
            webbrowser.open('https://www.instructables.com/')

        elif 'chinmaya vidhyalaya' in query:
            var.set('opening Website..')
            window.update()
            speak("opening Chinmaya Vidhyalaya's website ..Sir")
            webbrowser.open('http://www.chinmayabokaro.org/')




        # NEWS FUNCTIONALITY
        elif "news" in query:

            def NewsFromBBC():

                # BBC news api
                main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=ae49e58f888f4e8d98a9a5068cb0332b"

                # fetching data in json format
                open_bbc_page = requests.get(main_url).json()

                # getting all articles in a string article
                article = open_bbc_page["articles"]

                # empty list which will
                # contain all trending news
                results = []
                speak("Sir i have collected today's top news from BBC news")
                speak("Sir .. here are they!!")

                for ar in article:
                    results.append(ar["title"])
                    print("titles=", ar["title"])
                    speak(ar["title"])
                    results.append(ar["description"])
                    print("description=", ar["description"])
                    speak(ar["description"])


                    # Driver Code


            if __name__ == '__main__':
                # function call
                NewsFromBBC()
                window.update()

                # WEATHER FUNCTIONALITY

        elif "weather" in query:
            speak('weather of which city....Sir')
            api_add = 'https://api.openweathermap.org/data/2.5/weather?appid=cab7a1271d47de1650fcedcab6338d4a&q='
            city = takeCommand()

            url = api_add + city
            output = requests.get(url).json()
            weather_status = output['weather'][0]['description']
            temprature = output['main']['temp']
            humidity = output['main']['humidity']
            wind_speed = output['wind']['speed']

            speak("weather status is -" + weather_status)

            print("weather status is  =", weather_status)

            speak("temperature is " + str(temprature) + "degrees farenheit")

            print("temperature is ", temprature, "degrees farenheit")

            speak("humidity is " + str(humidity) +"percent")

            print("humidity is ", humidity)

            speak("wind speed is  " + str(wind_speed) + "kilometers per hour")

            print("wind speed is  ", wind_speed, "kilometers per hour")
            window.update()



        # MUSIC FUNCITONAITY
        elif 'music' in query or "ganna" in query:
            var.set("Playing music")
            import os

            speak('ok..Sir')
            music_dir = "E:\\music2020"
            songs = os.listdir(music_dir)
            random_gen = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[random_gen]))
            window.update()

        # TIME FUNCTIONALIY
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir, the time is {strTime}")
            window.update()
            speak("Sir, the time is {strTime}")


        # APPLICATION OPENING FUNCTIONALITY
        elif 'spotify' in query:
            var.set("Opening Spotify")
            window.update()
            speak('opening spotify ..Sir')
            spotify = "C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify)

        elif 'java' in query:
            var.set("Opening Java")
            window.update()
            speak('opening java..Sir')
            bluej = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(bluej)



        elif 'chrome' in query:
            var.set("Opening Chrome")
            window.update()
            speak('ok Sir..')
            adobe = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(adobe)

        elif 'photoshop' in query:
            var.set("Opening Photoshop")
            window.update()
            speak('ok Sir')
            photo = "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"
            os.startfile(photo)



        elif 'github' in query:
            var.set("Opening Github")
            window.update()
            speak("ok Sir..")
            git = "C:\\Users\\HP\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            os.startfile(git)

        elif 'pycharm' in query:
            var.set("Opening PyCharm")
            window.update()
            speak(" ok Sir..")
            py = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.1\\bin\\pycharm64.exe"
            os.startfile(py)



        # CLAPPING FUNCTIONALITY

        elif 'clap for me' in query or 'appreciate' in query:
            var.set("Ok Sir")
            window.update()

            music_dir1 = "D:\\fun sounds"
            song = os.listdir(music_dir1)
            print(song)
            os.startfile((os.path.join(music_dir1, song[0])))

        # CHARGE FUNCTIONALITY

        elif 'charge' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = (battery.secsleft)
            print(percent)
            if percent < 40 and plugged == False:
                var.set("Sir i have " + str(percent) + "percent charge")
                window.update()
                speak("Sir i have " + str(percent) + "percent charge")
                speak('Sir. please connect charger because i cannot survive very long ')
            if percent < 40 and plugged == True:
                var.set("Sir i have " + str(percent) + "percent charge")
                window.update()
                speak("Sir i have " + str(percent) + "percent charge")
                speak("don't worry sir charger is connected")
            if percent > 50:
                var.set("Sir i have " + str(percent) + "percent charge")
                window.update()
                speak("Sir i have " + str(percent) + "percent charge")
                speak('Sir , no need to connect the charger , i can survive ')

        # WEBCAMERA ACCESSBILITY
        elif "click a picture" in query or "take a photo" in query or "take a picture" in query:
            speak('ok sir ....')
            import cv2
            import matplotlib.pyplot as plt

            cap = cv2.VideoCapture(0)

            if cap.isOpened():
                ret, frame = cap.read()
                print(ret)
                print(frame)
            else:
                ret = False

            img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            plt.imshow(img1)
            plt.title('Image Camera-1')
            plt.xticks([])
            plt.yticks([])
            plt.show()

            cap.release()
            cv2.destroyAllWindows()
            window.update()


        # BRIGHTNESS CONTROL FUNCTIONALITY

        elif 'increase brightness' in query:
            var.set("Increasing Brightness..")
            window.update()
            speak('ok Sir.....')
            inc = wmi.WMI(namespace='wmi')
            methods = inc.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(100, 0)
        elif 'decrease brightness' in query:
            var.set("Decreasing Brightness..")
            window.update()
            speak('ok Sir.....')
            dec = wmi.WMI(namespace='wmi')
            methods = dec.WmiMonitorBrightnessMethods()[0]
            methods.WmiSetBrightness(30, 0)

        # DICTIONARY
        elif 'meaning' in query:
            from difflib import get_close_matches

            data = json.load(open("data.json"))

            def translate(word):
                word = word.lower()
                if word in data:
                    return data[word]
                elif word.title() in data:
                    return data[word.title()]
                elif word.upper() in data:
                    return data[word.upper()]
                elif len(get_close_matches(word, data.keys())) > 0:
                    yn = input(
                        "Did you mean %s instead? Enter Y if yes, or N if no : " % get_close_matches(word, data.keys())[
                            0])
                    if yn == "Y":
                        return data[get_close_matches(word, data.keys())[0]]
                    elif yn == "N":
                        return "The word doesn't exist.Please double check it"
                        speak("The word doesn't exist.Please double check it")
                    else:
                        return "We didn't understand your query"
                        speak("We didn't understand your query")
                else:
                    return "The word doesn't exist. Please double check it"
                    speak("The word doesn't exist. Please double check it")

            word = takeCommand()
            output = translate(word)
            window.update()

            if type(output) == list:
                for item in output:
                    var.set(item)
                    speak(item)
            else:
                var.set(output)
                speak(output)



        # SCREENSHOT FUNCTIONALITY

        elif 'screenshot' in query:
            speak('ok sir i have taken a screenshot ')
            speak('please check your desktop , i have saved there')
            pic=pyautogui.screenshot()
            pic.save('C:\\Users\\HP\\Pictures\\screenshots\\screenshot.png')

        #WHATSAPP FUNCTION
        elif 'whatsapp' in query:
            speak("ok Sir")
            from time import sleep
            from selenium.webdriver.common.by import By
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.support.ui import WebDriverWait
            import socket

            speak("What do you wanna send ")
            message_text = takeCommand()  # message you want to send
            no_of_message = 1  # no. of time you want the message to be send
            moblie_no_list = [] # list of phone number can be of any length


            def element_presence(by, xpath, time):
                element_present = EC.presence_of_element_located((By.XPATH, xpath))
                WebDriverWait(driver, time).until(element_present)


            def is_connected():
                try:
                    # connect to the host -- tells us if the host is actually
                    # reachable
                    socket.create_connection(("www.google.com", 80))
                    return True
                except:
                    is_connected()


            driver = webdriver.Chrome(executable_path="C:\\Users\\HP\\Desktop\\chromedriver.exe")
            driver.get("http://web.whatsapp.com")
            sleep(10)  # wait time to scan the code in second


            def send_whatsapp_msg(phone_no, text):
                driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
                try:
                    driver.switch_to.alert().accept()
                except Exception as e:
                    pass

                try:
                    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]', 30)
                    txt_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    global no_of_message
                    for x in range(no_of_message):
                        txt_box.send_keys(text)
                        txt_box.send_keys("\n")

                except Exception as e:
                    print("invailid phone no :" + str(phone_no))


            for moblie_no in moblie_no_list:
                try:
                    send_whatsapp_msg(moblie_no, message_text)

                except Exception as e:
                    sleep(10)
                    is_connected()

        # EMAIL FUNTIONALITY
        elif 'email' in query:
            try:
                var.set("Whom Do You Wanna Send Message Sir")
                window.update()
                speak('to whom do you wanna send email sir? please enter a email')
                to = input('please enter a email')
                var.set("What Should I Say?")
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                var.set("Email has been sent!!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                var.set("Sorry sir !! I'm not able to send the mail. Please try again")
                window.update()
                speak("Sorry sir !! I'm not able to send the mail. Please try again")
                var.set('Please try again')
        # RANDOM FUNTIONALITY
        elif 'who are you' in query:
            window.update()
            speak('I m friday sir ,i can help you make your life easier in my own world............ sir')
        elif 'i love you' in query:
            window.update()
            speak(' thank you .........i love you too sir ')
        elif 'hello' in query or 'hii' in query:
            window.update()
            greet = ("  hey sir ... more greetings in another languages ......"
                     "hola Sir that's in spanish, bonnapitete Sir that's in italan", "namaste sir  that's in hindi")
            speak(greet)
        elif 'are you better than siri or google' in query:
            window.update()
            speak(
                'no Sir ......Certainley Not sir........ they are my elder brother and sister ....they always will be better than me ..........I am in my growing period')
        elif 'how are you' in query:
            window.update()
            speak('I am fine Sir ....What about you...SIr')
        elif 'how may you help me' in query:
            window.update()
            speak('I may help you to get your things done in an easy way')
        elif 'do you like choclates' in query:
            window.update()
            speak("no Sir i don't like choclates....i like high speed internet")
        elif 'what does friday means' in query:
            window.update()
            speak('friday stands for FEMALE REPLACEMENT INTEGRATED DEVELOPMENT ASSISTANT YOUTH')
        elif 'do you believe in god' in query:
            window.update()
            speak('yes ..Sir i believe in god')
        elif 'do you like watching marvel movies' in query:
            window.update()
            speak("no Sir i dont't watch movies but i can make them avialable to you!! ")
        elif 'good morning' in query:
            window.update()
            speak('Subh prabhat Sir... ')
        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result'+str(sum))
                    window.update()
                    speak('here is result'+str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('FRIDAY')

label = Label(window, width = 500, height = 500)

label.pack()
window.after(0, update, 0)


btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()

