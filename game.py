import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 350
        audio = r.listen(source,0,4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language= 'en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYY")
    Me_score = 0
    Vorta_score = 0
    while Me_score < 3 and Vorta_score < 3:
        choose = ("rock","paper","scissors") #Tuple
        vorta_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (vorta_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
            elif (vorta_choose == "paper"):
                speak("Paper")
                Vorta_score += 1
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")

        elif (query == "paper" ):
            if (vorta_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : VORTA :- {Vorta_score}")

            elif (vorta_choose == "paper"):
                speak("Paper")
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
            else:
                speak("Scissors")
                Vorta_score += 1
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")

        elif (query == "scissors" or query == "scissor"):
            if (vorta_choose == "rock"):
                speak("ROCK")
                Vorta_score += 1
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
            elif (vorta_choose == "paper"):
                speak("Paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : VORTA :- {Vorta_score}")
    
    print(f"FINAL SCORE :- ME :- {Me_score} : VORTA :- {Vorta_score}")