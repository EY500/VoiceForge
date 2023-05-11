import speech_recognition as sr
import pyttsx3

rec = sr.Recognizer()
tts = pyttsx3.init()


def speak(word):
    tts.setProperty('rate', 135)
    tts.setProperty('volume', 0.8)

    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[0].id)

    tts.say(str(word))
    tts.runAndWait()
    tts.stop()
                    
while True:

    print("Recording...")
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=2)
        source.pause_treshold = 1
        audio = rec.listen(source, phrase_time_limit=None, timeout=None)
        
    try:
        transcript = rec.recognize_google(audio)
        
        if transcript == 'exit':
            break
        
        else:
            print(transcript)
            speak(transcript)

    except:
        print("An error occured...")
    