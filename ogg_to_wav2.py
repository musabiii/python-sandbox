from pydub import AudioSegment
import os

def ogg_to_wav(ogg_filename):
    wav_filename = ogg_filename.replace('.ogg', '.wav')
    audio = AudioSegment.from_file(ogg_filename)
    audio.export(wav_filename, format='wav')

path = os.path.abspath("./");
file_path = os.path.join(path,"new_file_ru_2.ogg")

ogg_to_wav("new_file_ru_2.ogg")
