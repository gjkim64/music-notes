# FakeBass experiment sketches (original note: fakebass.txt)
# Unedited scratch code kept for reference: `play_music` is not defined here,
# so the threading part will not run as-is.

import sounddevice as sd

import soundfile as sf
import threading

from datetime import datetime



data, fs = sf.read('test.wav', dtype='float32')
arraylength = len(data)
# keep playing in 100 segments
duration = arraylength / fs
segment_data_length = int(arraylength / 10)
for i in range (10):
 j = i * segment_data_length
 segment = data[j:(j+segment_data_length-1)]
 #print (j) 
 #print (j+segment_data_length-1)
 #print (len(segment))
 sd.play(segment, fs)
 
 
def count_and_print ():
 for i in range (100000):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("Current Time =", current_time)

filename='test.wav'

t = threading.Thread(target=play_music)

t.start()
count_and_print()




import numpy as np
import librosa
import matplotlib.pyplot as plt

import scipy.stats

y, sr = librosa.load('super.wav', duration=30)
onset_env = librosa.onset.onset_strength(y, sr=sr)
tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

prior = scipy.stats.uniform(30, 300)  # uniform over 30-300 BPM
utempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, prior=prior)
utempo

dtempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr,aggregate=None)

x = librosa.onset.onset_detect(y, sr, onset_envelope=onset_env, units='time')






