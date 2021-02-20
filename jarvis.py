import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    '''
    This function is used to speak the words or sentenses for jarvis
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    for wishing me good morning,afternoon and evening
    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    
    elif hour>=12 and hour<17:
        speak("Good Afternoon sir")    

    else:
        speak("Good Evening sir")
    speak("My name is jarvis, speed one terahertz, memory one terabytes, how can i help you?")

def takeCommand():
    '''
    it takes microphone audio as input
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
        











if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on our input query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=DFGDGDFGDFGFDVS")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_dir = "F:\\PD and SD card\\MMW sdcard\\MYMusics"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            code_path = "C:\\Users\\Mohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'open browser' in query:
            browser_path = "C:\\Users\\Mohit\\AppData\\Local\Mozilla Firefox\\firefox.exe"
            os.startfile(browser_path)
            