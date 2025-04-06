import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def openCommand(c):
    if "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    if c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Hello from Jarvis")

    while True:
        #Listening to auido
        r = sr.Recognizer()

        #Recognizing speech using recognize_google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1.5)
                print("Recognizing...")
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                print(word.lower())
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source)
                    print("Recognizing...")
                    command = r.recognize_google(audio)
                    print(command)

                    openCommand(command)
        except Exception as e:
            print(f"Jarvis couldn't recognize you {e}")