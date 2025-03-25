import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime

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
        r.energy_threshold = 400
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Please say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" or "you can sleep" in query:
                    speak("Ok boss, You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello boss, how are you?")
                elif "i am fine" in query:
                    speak("That's great, boss")
                elif "how are you" in query:
                    speak("Perfect, boss")
                elif "who made you" in query:
                    speak("I am made by Group 1 of TE IT")
                elif "who are you" in query:
                    speak("I am VORTA AI Voice Assistant and I am here to assist you")
                elif "thank you" or "thanks" in query:
                    speak("You are welcome, boss")
                elif "bye" or "goodbye" in query:
                    speak("Hope you have a great day")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "weather in mumbai"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    weather = data.find("div", class_ = "BNeawe").text
                    speak(f"current {search} is {weather}")

                elif "the time" or "current time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Boss, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep, boss")
                    exit()