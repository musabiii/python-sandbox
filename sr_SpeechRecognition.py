# importing libraries
import speech_recognition as sr # numpy also require
import os
import soundfile as sf


# create a speech recognition object
r = sr.Recognizer()

def transcribe_audio(path):
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        text = r.recognize_google(audio_listened, language='ru-RU')
    return text

def ogg_to_wav(ogg_file_path):
    data, samplerate = sf.read(ogg_file_path)
    wav_file_path = ogg_file_path + ".wav"
    sf.write(wav_file_path, data, samplerate)
    return wav_file_path

def ogg_to_text(file_name):
    workdir = os.path.abspath("./");
    ogg_file_path = os.path.join(workdir, file_name)

    wav_file_path = ogg_to_wav(ogg_file_path)

    txt = transcribe_audio(wav_file_path)

    if os.path.exists(wav_file_path):
        os.remove(wav_file_path)

    return txt


file_name = "files/new_file_ru.ogg"

txt = ogg_to_text(file_name)


print(txt);
