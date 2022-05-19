import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import datetime
import pywhatkit as kit
from translate import Translator
# from englisttohindi.englisttohindi import EngtoHindi
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
from getpass import getpass
import  time



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[1])
rate = engine.getProperty("rate")
engine.setProperty("rate",180)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        speak("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising...")
        speak("recognising...")

        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print("say that again")
        speak("say again please")
        return "none"
    return query


def takecommandmain():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("..")

        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("...")

        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        print("say that again")

        return "none"
    return query

def reminder():
    hour = int(datetime.datetime.now().hour)
    if hour==21:
        speak("your eating time")
    elif hour==22:
        speak("sleeping time")

def Task():
    
    while True:
        query = takecommand().lower()
        if 'jarvis' in query:
            speak("yes i am listening")

        if 'thank you' in query:
            speak("your most welcome")
            run = False
        try:
            if 'wikipedia' in query:
                speak('searching wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
        except Exception as e:
            speak(f"there is no page named {query}")

        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'show me monitor' in query:
            webbrowser.open("https://www.amazon.in/Lenovo-Ultraslim-Monitor-FreeSync-Customization/dp/B097MHBXTG?ref_=ast_sto_dp&th=1&psc=1")

        if 'play bella ciao' in query:
            webbrowser.open("https://www.youtube.com/watch?v=0aUav1lx3rA&list=RD0aUav1lx3rA&start_radio=1")
        
        elif 'open instagram' in query:
            speak("type the password to open your insta account")
            password = input()
            if password == 'rhushi@2003':
                speak("opening instagram")
                webbrowser.open("https://www.instagram.com/rhushi_programmer/")
            else:
                speak("you can not access this account deu to security purpose")

        elif 'open my site' in query:
            webbrowser.open("rhushikesh.pythonanywhere.com")

        elif 'open my book store site' in query:
            webbrowser.open("bookbecho.pythonanywhere.com")

        elif 'open facebook' in query:
            speak("type the password to open your facebook account")
            password = input()
            if password == 'rhushi@2003':
                speak("opening facebook")
                webbrowser.open("https://www.facebook.com/rhushikesh.nandodkar.3")
            else:
                speak("you can not access this account deu to security purpose")

        elif 'open google' in query:
            webbrowser.open("google.com")



        elif 'play music' in query:
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'play movie' in query:
            video_dir = 'C:\movie\main'
            movie = os.listdir(video_dir)
            print(movie)
            os.startfile(os.path.join(video_dir, movie[0]))

        elif 'play money heist episode 1' in query:
            speak("type the password if you want to watch that video")
            password = input()
            if password == 'rhushi@2003':
                video_dir = 'C:\\Users\\91942\\Videos\\Telegram Video'
                movie = os.listdir(video_dir)
                print(movie)
                os.startfile(os.path.join(video_dir, movie[8]))
            else:
                speak("i can not play this video in front of you because you don't have permission to watch that video")

        # elif 'open code' in query:
        #     speak("opening code")
        #     codefile = 'C:\Users\91942\AppData\Local\Programs\Microsoft VS Code\Code.exe'
        #     os.startfile(codefile)

        elif 'what are you' in query:
            speak("i am jarvis i am the your personal assistent")
        elif 'what can you do for me' in query:
            speak("i can make your life easy by doing your simple and boring works on computer you have to tell me about your work and the just chill")
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif 'open code' in query:
            speak("opening vs code")
            codepath = "E:\\Users\\91942\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            speak("opening chrome")
            codepath = "E:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codepath)

        elif 'open full stack' in query:
            speak("opening full stack file")
            codepath = "E:\\Users\\91942\\Desktop\\jarvis\\mern"
            os.startfile(codepath)

        elif 'open first django project' in query:
            speak("opening python project file")
            codepath = "E:\\Users\\91942\\Desktop\\jarvis\\django1\\hello"
            os.startfile(codepath)

        elif 'open my portfolio site file' in query:

            codepath = "E:\\Users\\91942\\Desktop\\jarvis\\portfolio\\project"
            os.startfile(codepath)

        elif 'open django tutorial file' in query:
            speak("opening django tutorial file")
            codepath = "E:\\Users\\91942\\Desktop\\jarvis\\New folder (5)\\project"
            os.startfile(codepath)

        elif 'favourite music' in query:
            speak("playing your favorite music")
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[11]))
        elif 'play despacito' in query:
            speak("playing despacito")
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[11]))
        elif 'play love me like you do' in query:
            speak("playing love me like you do")
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[6]))
        elif 'play ride' in query:
            speak("playing ride")
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)


            os.startfile(os.path.join(music_dir, songs[14]))

        elif 'play baby song' in query:
            speak("playing baby song")
            music_dir = 'C:\music'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[10]))

        elif 'who is lena' in query:
            speak("leena is sister of worlds richest person she is an english teacher in topiwala highschool maalavan")

        elif 'who is sachin the billion dreams' in query:
            speak("he is the most hopeless person he is taklyaa also he have big spectacle and his nickename is dolyaa")

        elif 'send message' in query:
            speak("what is message?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening....")
                r.pause_threshold = 1
                audio = r.listen(source)
                message = r.recognize_google(audio, language='en-in')

                hour = int(datetime.datetime.now().hour)
                minute = int(datetime.datetime.now().minute) + int(1)
                print(f"user said : {message}")

                kit.sendwhatmsg("+918329909052", f"{message}", hour, minute)

        elif 'translate in german' in query:
            speak("what is sentence?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening....")
                r.pause_threshold = 1
                audio = r.listen(source)
                trance = r.recognize_google(audio, language='en-in')
                print(f"user said : {trance}")
                translator = Translator(to_lang="german")
                translation = translator.translate(trance)
                print(translation)
                speak(f"translation is {translation}")

        elif 'translate in italian' in query:
            speak("what is sentence?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening....")
                r.pause_threshold = 1
                audio = r.listen(source)
                trance = r.recognize_google(audio, language='en-in')
                print(f"user said : {trance}")
                translator = Translator(to_lang="italian")
                translation = translator.translate(trance)
                print(translation)
                speak(f"translation is {translation}")

        if 'tum mar jao' in query:
            speak("tere baap ka maal he kya")

        elif 'translate in spanish' in query:
            speak("what is sentence?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening....")
                r.pause_threshold = 1
                audio = r.listen(source)
                trance = r.recognize_google(audio, language='en-in')
                print(f"user said : {trance}")
                translator = Translator(to_lang="spanish")
                translation = translator.translate(trance)
                print(translation)
                speak(f"translation is {translation}")

        # elif 'translate in hindi' in query:
        #     speak("what is sentence?")
        #     r = sr.Recognizer()
        #     with sr.Microphone() as source:
        #         print("listening....")
        #         r.pause_threshold = 1
        #         audio = r.listen(source)
        #         hindi = r.recognize_google(audio, language='en-in')
        #         print(f"user said : {hindi}")
        #         message1 = hindi
        #         res = EngtoHindi(message1)
        #         print(res.convert)
        #         speak(res.convert)

        elif 'google search' in query:
            speak("what to search")
            r = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    print("listening....")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                    qwer = r.recognize_google(audio, language='en-in')
                    print(f"user said : {qwer}")
                    user_querya = qwer
                    url = 'https://google.com/search?q=' + user_querya

                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
                    }

                    page = requests.get(url, headers=headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    result = soup.find(class_='Z0LcW XcVN5d').get_text()
                    print(result)
                    speak(result)

            except Exception as e:
                speak("please go to doctor and check your health")

        elif 'live score' in query:

            url = 'https://www.cricbuzz.com/cricket-match/live-scores/recent-matches'

            while True:
                time.sleep(5)
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'lxml')
                score_card = soup.find('div', class_='cb-ovr-flo').text
                speak(score_card)

        elif 'go to hell' in query:
            speak(f"you {query}")

        elif 'how are you' in query:
            speak("i am fine what about you")

        elif 'i am fine' in query:
            speak("thats good")

        elif 'i am not fine' in query:
            speak("whats the problem")

        elif 'i want' in query:
            speak("if you dont have something then think about what you have and be greatfull")


        elif 'how to' in query:
            while True:
                speak("collecting data from internet")
                op = query.replace("jarvis", "")
                max_result = 1
                how_to = search_wikihow(op, max_result)
                assert len(how_to) == 1
                how_to[0].print()
                speak(how_to[0].summary)
                break
       
        break

def taskexite():
    speak("your most welcome")

if __name__ == "__main__":

    while True:

        permission = takecommandmain().lower()
        if 'alexander' in permission:
            Task()

        elif 'thank you' in permission:
            taskexite()
        


