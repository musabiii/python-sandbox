import soundfile as sf
import os
import numpy as np

path = os.path.abspath("./");
file_path = os.path.join(path,'new_file_ru.ogg')
file_write = os.path.join(path,'new_file_ru_ogg.wav')

data, samplerate = sf.read('new_file_ru.ogg')
sf.write('new_file_ru_ogg.wav', data, samplerate)
