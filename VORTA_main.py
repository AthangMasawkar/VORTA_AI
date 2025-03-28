import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
import speedtest_cli

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME BOSS ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Please say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query or "you can sleep" in query:
                    speak("Ok boss, You can call me anytime")
                    break

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done boss")
                    speak(f"Your new password is {new_pw}")

                elif "hello" in query:
                    speak("Hello boss, how are you?")
                elif "i am fine" in query:
                    speak("That's great boss")
                elif "how are you" in query or "how r u" in query:
                    speak("Perfect boss")
                elif "who made you" in query:
                    speak("I am made by Group 1 of TE IT")
                elif "who are you" in query:
                    speak("I am VORTA AI Voice Assistant and I am here to assist you")
                elif "thank you" in query or "thanks" in query:
                    speak("You are welcome boss")
                elif "bye" in query or "goodbye" in query:
                    speak("Hope you have a great day")

                elif "open" in query or "launch" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closewebapp
                    closewebapp(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "the time" in query or "current time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Boss, the time is {strTime}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done boss")

                elif "pause video" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play video" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute video" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up boss")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down boss")
                    volumedown()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("vorta","")
                    speak("You told me "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read())

                elif "tired" in query or "songs" in query or "song" in query:
                    speak("Playing your favourite songs boss")
                    a = (1,2,3,4,5,6,7)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=FFbc-jXkADs")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=hjfzFVw2Zjo")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=S0WPSYFm7iE")
                    elif b==4:
                        webbrowser.open("https://www.youtube.com/watch?v=I5t894l5b1w")
                    elif b==5:
                        webbrowser.open("https://www.youtube.com/watch?v=MkABeVCv4lw")
                    elif b==6:
                        webbrowser.open("https://www.youtube.com/watch?v=EGExS_0qQq0")
                    elif b==7:
                        webbrowser.open("https://www.youtube.com/watch?v=-mKSeBJ_okY")

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("vorta","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (y/n)")
                    if shutdown == "y":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "n":
                        break

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                    
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi download speed in MB is ",download_net)
                    print("Wifi Upload Speed in MB is ", upload_net)
                    speak(f"Wifi download speed in MB is {download_net}")
                    speak(f"Wifi Upload speed in MB is {upload_net}")

                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO\n"))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\Athang\\OneDrive\\Desktop\\VORTA_AI\\FocusMode.py")
                    else:
                        pass

                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                elif "finally sleep" in query:
                    speak("Going to sleep, boss")
                    exit()