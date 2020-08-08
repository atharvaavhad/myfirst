import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from tkinter import *
import webbrowser
import os
from tkinter import ttk
import smtplib
import pyautogui
import sys
def philis():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am philis . Please tell me how may I help you")

    def takeCommand():
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.0
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-uk')
            print(f"User said: {query}\\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            speak("Say that again please...")
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('atharvaavhad2010@gmail.com', 'Jayshreekrishna')
        server.sendmail('atharvaavhad2010@gmail.com', to, content)
        server.close()

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'hey' in query:
                speak('What? I can do')

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                while True:
                                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                                speak(f",the time is {strTime}")

            elif 'open atom' in query:
                codePath = r"C:\Users\sa group\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc\Atom.lnk"
                os.startfile(codePath)

            elif 'open suv' in query:
                codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk"
                os.startfile(codePath)
            elif 'to click' in query:
                pyautogui.doubleClick()

            elif 'thanks' in query:
                speak("welcome")

            elif 'single' in query:
                pyautogui.click()

            elif 'type' in query:
                speak("what I should type?")
                a = takeCommand()
                pyautogui.typewrite(a)

            elif "net" in query:
                speak('pyautogui press enter')
                pyautogui.keyDown("enter")

            elif 'exit' in query:
                sys.exit()

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "atharvaavhad2010@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I'cant send this email")
philis()
