import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import random
import re

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def print_multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
        speak(f"{number} {i}s are {number * i}")
        

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning ,  how can i help you ?")
    elif hour>=12 and hour<18:
        speak("Good afternoon!,  how can i help you ?")
    else:
        speak("Good Evening! ,  how can i help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"user said : {query}\n")

    except Exception as e:
        speak("Sorry i can't recognized , please try again")
        return "none"
    return query

if __name__ == "__main__" :
    wishme()
    loop=True
    while loop==True:
        query = takeCommand().lower()
    #logics
        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("opening youtube for u sir")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google for u sir")
        
        elif 'open source bin' in query:
            webbrowser.open("https://sourceb.in/")
            speak("opening sourcebin for u sir")
        
        elif 'open my github' in query:
            webbrowser.open("https://github.com/Strange144")
            speak("opening your gihub sir")
        
        elif 'open my insta' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("opening your instagram sir")
        
        elif 'open my linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/ansul-joshi-8b2758286/")
            speak("opening your linkedin sir")

        elif 'play music' in query:
            speak("starting music")
            music_dir='C:\\Users\\joshi\\OneDrive\\Desktop\\songs'
            songs=os.listdir(music_dir)
            number_of_songs=len(songs)-1
            number=random.randint(0,number_of_songs)
            os.startfile(os.path.join(music_dir,songs[number]))
        
        elif 'laugh like sachin' in query:
            sachin='C:\\Users\\joshi\\OneDrive\\Desktop\\songs\\sachin.mpeg'
            os.startfile(sachin)

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%m:%S")
            speak(f"sir , the time is {strtime}")

        elif 'open vs code' in query:
            speak("opening vs code")
            codepath="C:\\Users\\joshi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'open word' in query:
            speak("opening word ")
            mcodepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(mcodepath)

        elif 'table of' in query:
            match = re.search(r'\btable of (\d+)\b', query)
            if match:
                number = int(match.group(1))
                print_multiplication_table(number)
            else:
                print("Number not found or invalid format in query.")

        elif 'who are you' in query:
            speak("I am your faithful voice assistant, designed and programmed by Ansul Joshi to assist you in various tasks. With my advanced artificial intelligence capabilities, I am equipped to understand and respond to your commands efficiently. Whether it's retrieving information, managing tasks, or providing assistance, I am here to make your life easier. Feel free to interact with me and let me know how I can be of service to you!")

        elif 'who is anshul' in query:
            speak("Ansul or Ansul Joshi,is a 19 years old and currently pursuing his studies at Pillai College of Arts, Commerce, and Science. He possesses a profound passion for web development and has masterfully crafted me ! In his leisure time, he finds solace in the art of sketching and the strength gained from weight lifting. It's a pleasure to acquaint you with his esteemed presence!") 
            
        elif 'ram ram' in query:
            speak("Ram Ram bhai , kya haal !!")

        elif 'abaki bar' in query:
            excitement = "Modi Sarkar!!"  # Add exclamation marks for excitement
            speak(excitement.upper()) 
        # elif 'email to modiji' in query:
        #     try:
        #         speak("What should i say ?")
        #         content=takeCommand()
        #         to="joshideepak920@gmail.com"
        #         sendEmail(to,content)
        #         speak("Email has been sent !")
        #     except Exception as e:
        #         speak("Sorry Ansul , i am unable to sent this email")

        elif 'stop' in query:
            speak("deactivated")
            loop=False