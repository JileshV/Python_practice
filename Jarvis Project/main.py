import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello from Jarvis")

    while True:
        #Listening to auido
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        #Recognizing speech using recognize_google
        try:
            command = r.recognize_google(audio)
            print(command)
        except sr.UnknownValueError:
            print("Jarvis couldn't recognize you")
        except sr.RequestError as e:
            print(f"Jarvis error {e}")