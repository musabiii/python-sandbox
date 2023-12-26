import speech_recognition as sr
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

path = os.path.abspath("./");
file_path = os.path.join(path,"new_file_ru.wav")

# Reading Audio file as source
# listening the audio file and store in audio_text variable
with sr.AudioFile(file_path) as source:

    audio_text = r.record(source)

    print('Converting audio transcripts into text ...')
    text = r.recognize_google(audio_text, language='ru-RU')
    print(text)

