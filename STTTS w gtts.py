import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


rec = sr.Recognizer()

def speak(word):
    tts = gTTS(text=transcript, lang='en', tld='us')
    tts.save('output_gTTS.mp3')
    playdub = AudioSegment.from_mp3("output_gTTS.mp3")
    play(playdub)

while True:

    print("Recording...")
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=3)
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