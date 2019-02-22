import pysynth_b as ps
import simpleaudio as sa
import random
import sys
import copy
import os
import time
from pydub import AudioSegment

note1 = [("g4", -2)]
ps.make_wav(note1, fn = "chord1.wav")

note2 = [("b4", -2)]
ps.make_wav(note2, fn = "chord2.wav")

note3 = [("c", -2)]
ps.make_wav(note3, fn = "chord3.wav")

note4 = [("e", -2)]
ps.make_wav(note4, fn = "chord4.wav")

sound1 = AudioSegment.from_file("chord1.wav")
sound2 = AudioSegment.from_file("chord2.wav")
sound3 = AudioSegment.from_file("chord3.wav")
sound4 = AudioSegment.from_file("chord4.wav")

onetwo = sound1.overlay(sound2)
onetwothree = onetwo.overlay(sound3)
combined = onetwothree.overlay (sound4)

combined.export("combined.wav", format='wav')

wave_obj = sa.WaveObject.from_wave_file("combined.wav")
play_obj = wave_obj.play()
play_obj.wait_done()