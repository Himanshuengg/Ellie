import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os


#For information of predefined function press ctrl+Click on that function name


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id) # 1 for female voice



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    ''' Wish Me function wish you according to the timing '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning!!")

    elif hour >= 12 and hour < 17:
        speak(" Good Afternoon!!")   

    else:
        speak("Good Evening")

    speak("I am Ellie. Please tell me how i can help you.  !")    



def takeCommand():
    '''It take microphone input from the user and return string output'''
    
    r = sr.Recognizer() # this recognizer class help us to recognize audio
    with sr.Microphone() as sourse: # i will use sourse as microphone
        print("Listening.....")
        r.pause_threshold = 1 #while listening if i will take gap of 1 second, i will no finish the face 
        audio = r.listen(sourse)

        try:
            print("Recognizig.....")
            query = r.recognize_google(audio , language = 'en-in')
            print(f"User said : {query}\n")

        except Exception as e:
            #print(e)

            print("print that again please......")
            return "None"
        
        return query



if __name__ == "__main__":
    ''' This is the mai function '''

    wishMe()

    while True:
        query = takeCommand().lower()
        #speak("Himanshu is a good boy")

        # Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2) # It will take two lines from the wikipedia of searching text.
            speak("According to wikipedia")
            print(results) 
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open git' in query:
            webbrowser.open("https://github.com/Himanshuengg?tab=repositories")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'music' in query:
            music_dir = 'C:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'stop' in query:
            break

