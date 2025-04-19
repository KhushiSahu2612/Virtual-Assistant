import speech_recognition as aa
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyaudio
import pyjokes
import os
import AppOpener


listener = aa.Recognizer()

machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print('Listening...')
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if"Bixby" in instruction:
                instruction = instruction.replace('Bixby', " ")
            print(instruction)
    except:
        pass
    return instruction

def play_Bixby():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", " ")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('currnt time'+ time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        talk("Todays date "+ date)

    elif 'how are you ' in instruction:
        talk('I am Fine , how about you ')

    elif ' what is your name ' in instruction:
        talk('hello I am Bixby how can i help you ')

    elif "who is " in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human,1)
        print(info)
        talk(info)
    elif 'joke' in instruction:
        talk('ok Here is a joke for you ')
        print(pyjokes.get_joke())

        talk(pyjokes.get_joke())

    elif 'open microsoft Edge ' in instruction:
        talk('Opening Microsoft Edge Application')
        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
    
    elif("GOOGLE" in instruction ) or ("SEARCH" in instruction) or ("WEB BROWSER" in instruction) or ("CHROME" in instruction) or ("BROWSER" in instruction) :
        talk("Opening")
        talk("GOOGLE CHROME")
        print(".")
        print(".")
        os.system("chrome")


    elif 'Open Brave ' in instruction:
        talk('Opening Brave Application')
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

    elif 'open visual studio code' in instruction:
        talk('Opening Visual Studio Code Application ')
        os.startfile("C:\\Users\\tappu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
    elif 'open Whatsapp' in instruction:
        talk('Opening Whatsapp')
        from AppOpener import open ,close
        open("Whatsapp") # opens whatsapp

    elif "fuck you " in instruction:
        
        talk("Hello Bixboy")
    else:
        talk('please repeat ')    


play_Bixby()