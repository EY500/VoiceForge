import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import pydub 


wit_api_key = 'RAWZEC4AYA5JDCG4ZTY63ARKLZLHFDZK'

rec = sr.Recognizer()
p = pyaudio.PyAudio()


device_count = p.get_device_count()

for i in range(device_count):
    device_info = p.get_device_info_by_index(i)
    device_name = device_info['name']
    print(f"Device {i}: {device_name}")
    
output_device_index = int(input("Select Output device as 'Cable Input' : "))

def play_sound(audio_output):
    
    p = pyaudio.PyAudio()

    sound = pydub.AudioSegment.from_file(audio_output)

    audio_data = sound.raw_data

    sample_rate = sound.frame_rate
    sample_width = sound.sample_width
    channels = sound.channels

    device_info = p.get_device_info_by_index(output_device_index)
    device_name = device_info['name']
    device_id = device_info['index']

    stream = p.open(format=p.get_format_from_width(sample_width),
                channels=channels,
                rate=sample_rate,
                output=True,
                output_device_index=output_device_index)

    stream.write(audio_data)
    stream.stop_stream()
    stream.close()
    p.terminate()



def speak(word):
    tts = gTTS(text=transcript, lang='en', tld='us')
    tts.save('output_gTTS.mp3')
    play_sound('output_gTTS.mp3')

while True:

    print("Recording...")
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=2)
        source.pause_treshold = 1
        audio = rec.listen(source, phrase_time_limit=None, timeout=None)
        
    try:
        print('...')
        transcript = rec.recognize_wit(audio, key=wit_api_key)
        
        if transcript == 'Exit':
            print('Exiting...')
            break
        
        else:
            print('You said : ', transcript)
            speak(transcript)

    except:
        print("An error occured...")