# importing libraries
import speech_recognition as sr
import os

# create a speech recognition object
r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = r.recognize_google(audio_listened, language='ru-RU')
    return text

path = os.path.abspath("./");
file_path = os.path.join(path,"new_file_ru.wav")
print(path);
txt = transcribe_audio(file_path)
print(txt);
