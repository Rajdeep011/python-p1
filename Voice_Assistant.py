
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google_cloud(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand audio")
sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    engine.say(x)
    engine.runAndWait()

speechtx("hello welcome to Wscubetech")


if __name__ == '__main__':

    if  "hey peter" in sptext().lower():
        data1= sptext().lower()
        while True:
            
        if "what is your name" in data1:
            name = " my name is peter "
            speechtx(name)

        elif "old are you" in data1:
             age = "i am two years old"
             speechtx(age)

        elif 'time' in data1:
             time = datetime.datetime.now().strftime("%I%M%p")
             speechtx(time)
        elif 'youtube' in data1:
             youtube = webbrowser.open("https://www.youtube.com/")

        elif 'joke' in data1:
              joke_1 = pyjokes.get_joke(language= "en", category="natural")
              speechtx(joke_1)
        elif 'play song' in data1:
              add = "C:\Users\Mahakaal\Music"
              listensong = os.listdir(add)
              print(listensong)
              os.startfile(os.path.join(add, listensong[0]))
        elif "exit" in data1:
            speechtx("thank you")

        time.sleep(10)

    else:
        print("thank you")
