# Advanced Project 1 --> Sentinel ( Jarvis )
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import music_library
from gtts import gTTS
tts = gTTS('hello')
tts.save('hello.mp3')


recognizer = sr.Recognizer() # this is a class which helps in bringing up the speech recognition function.
engine = pyttsx3.init() # initialising the pyttsx3 module in python


"""Changing Voice from pyttsx"""
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 0 for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


NEWS_API = "0ee8950d496548a3b312349c5e5d1a7a" # Use your news api key -->> newsapi.org

def speak(text):
    engine.say(text)
    """VOICE"""
    engine.runAndWait()

def speak_new(text):
    pass

def process_command(c):
    print(c.lower())  # Print the recognized command for debugging

    if "bye" in c.lower():
        speak("Goodbye! Shutting down.")
        exit()  # Exit the program

    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open twitter" in c.lower() or "open x" in c.lower():
        webbrowser.open("https://twitter.com")

    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif "open github" in c.lower():
        webbrowser.open("https://github.com")

    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")

    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com")

    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")

    elif "open reddit" in c.lower():
        webbrowser.open("https://reddit.com")

    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")

    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")

    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chat.openai.com")

    elif "open python" in c.lower():
        webbrowser.open("https://www.python.org")

    elif "open bing" in c.lower():
        webbrowser.open("https://www.bing.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        req = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API}")

        if req.status_code == 200:
            data = req.json()  # Convert response to JSON
            articles = data.get("articles", [])  # Get the list of articles
            
            if not articles:  # Check if there are no articles
                speak("Sorry, I couldn't find any news at the moment.")
            else:
                speak("Here are the top news headlines.")
                for i, article in enumerate(articles[:5], 1):  # Limit to 5 headlines
                    headline = article.get("title", "No title available")  # Get the title safely
                    print(f"{i}. {headline}")  # Print it to the console for debugging
                    speak(f"Headline {i}: {headline}")
                    engine.runAndWait()  # Ensure it speaks each headline properly

        else:
            speak("Sorry, I couldn't fetch the news right now. Please try again later.")

    else:
        # If you have the OpenAI API you can put on the logic for handling any other request using GPT.
        speak("Sorry, I didn't recognize that command.")

if __name__ =="__main__":
    # print("hello") 
    speak("Initialising Sentinel...")
    # Listen for the word Sentinel...
    # obtain audio from the microphone
    while True:
        r = sr.Recognizer()
        print("Analyzing....")
        # recognize speech using Google
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source,timeout = 2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "sentinel"):
                speak("at your service!!")
                #listening for command
                with sr.Microphone() as source:
                    print("Sentinel on the roll......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    process_command(command)

        except Exception as e:
            print("Error {0}".format(e))
