import speech_recognition as sr
import webbrowser as web
import pyttsx3
from songs import music
import requests

tell=pyttsx3.init()
newsapi='11005069a380416dbeef078156c99400'
def speak(text):
    tell.say(text)
    tell.runAndWait()
def executor(c):
    if 'open google' in c.lower():
        web.open("https://google.com")
    elif 'open youtube' in c.lower():
        web.open('https://youtube.com')
    elif 'open likedin' in c.lower():
        web.open('https://www.linkedin.com/feed/')
    elif 'open facebook' in c.lower():
        web.open('https://facebook.com')
    elif 'open instagram' in c.lower():
        web.open('https://instagram.com')
    elif 'open whatsapp' in c.lower():
        web.open('https://web.whatsapp.com/')
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]  # Extract the song name
        link = music.get(song)
        if link:
            web.open(link)
    elif 'news' in c.lower():
        r = requests.get(f'https://newsapi.org/v2/everything?q=tesla&from=2024-09-29&sortBy=publishedAt&apiKey={newsapi}')
        data = r.json()
    
        if data["status"] == "ok":
            articles = data["articles"]
            for article in articles[:5]:  # Limit to the first 5 titles
                title = article["title"]
                print(f"Title: {title}")
                speak(title)
        else:
            speak("I couldn't retrieve the news at the moment.")


    print(c)
    pass
if __name__== '__main__':
    # recognize the word and start the process
    r=sr.Recognizer()
    while True:
        speak("Intializing....")
        print('Converting...')
         
        try:
            # Use the microphone as the source for input
            with sr.Microphone() as source:
                print("Please say something...")
                # Adjust for ambient noise and listen with specified timeouts
                r.adjust_for_ambient_noise(source, duration=1)
                Active = r.listen(source, timeout=2, phrase_time_limit=1) 

            # Recognize speech using Google Web Speech API
            text = r.recognize_google(Active)
            if  text.lower() == 'shannu':
                speak('Yes, how may I help you ?')
                
                with sr.Microphone() as sc:
                    print("Say your commands ")
                    command = r.listen(sc)
                    text=r.recognize_google(command)
                    executor(text)

        except Exception as e:
            print("Error; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Listening timed out, please try again.")
