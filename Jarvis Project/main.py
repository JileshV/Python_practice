import speech_recognition as sr
import webbrowser
import pyttsx3

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
    if "play rang" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=OdrOp7JwZiE&ab_channel=SaregamaMusic")

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