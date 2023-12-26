import soundfile as sf
import os
# import numpy as np

path = os.path.abspath("./");
file_path = os.path.join(path,'files/new_file_ru.ogg')
file_write = os.path.join(path,'files/new_file_ru_ogg.wav')

data, samplerate = sf.read(file_path)
sf.write(file_write, data, samplerate)

# data, samplerate = sf.read('./files/new_file_ru.ogg')
# sf.write('./files/new_file_ru_ogg.wav', data, samplerate)
