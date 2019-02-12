#https://stackoverflow.com/questions/260738/play-audio-with-python/34179010

import pysynth as ps
import sys
import random
import simpleaudio as sa
import copy

#the range of pitch that will be used to improvise, from low to high. 

bank = ["c3", "c#3", "d3", "d#3", "e3", "f3", "f#3", "g3", "g#3", "a3", "a#3", "b3",
          "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b",
          "c5", "c#5", "d5", "d#5", "e5", "f5", "f#5", "g5", "g#5", "a5", "a#5", "b5",
          "c6", "c#6", "d6", "d#6", "e6", "f6", "f#6", "g6", "g#6", "a6", "a#6", "b6"]

def bebop () :
	#This function will improvise based on set bebop scale and common patterns.
	#k = 12 will be c major, k = 13 will be c# major, k = 14 will be d major, and so on.

	k = 12

	fourbeats = [[(bank[k], 8), (bank[k-1], 16), (bank[k-2], 8),(bank[k+9], 16),(bank[k+7], -4)],
			[(bank[k+4], 8), (bank[k+2], 16), (bank[k], 8), (bank[k+11], 16),(bank[k+10], -4)],
			[(bank[k+7], 8), (bank[k+5], 16), (bank[k+4], 8),(bank[k+14], 16),(bank[k+12], -4)],
			[(bank[k+10], 8), (bank[k+9], 16), (bank[k+7], 8),(bank[k+17], 16),(bank[k+16], -4)],

			[(bank[k-2], 8), (bank[k+2], 16), (bank[k+5], 8), (bank[k+9], 16),(bank[k+7], -4)],
			[(bank[k+4], 8), (bank[k+7], 16), (bank[k+10], 8), (bank[k+14], 16),(bank[k+12], -4)],
			[(bank[k+7], 8), (bank[k+10], 16), (bank[k+14], 8), (bank[k+17], 16),(bank[k+16], -4)],

			[(bank[k+7], 8), (bank[k-2], 16), (bank[k+2], 8), (bank[k+5], 16), (bank[k+4], -4)],
			[(bank[k+10], 8), (bank[k+2], 16), (bank[k+5], 8), (bank[k+9], 16),(bank[k+7], -4)],
			[(bank[k+16], 8), (bank[k+7], 16), (bank[k+10], 8), (bank[k+14], 16),(bank[k+12], -4)],

			[(bank[k+9], 8), (bank[k+5], 16), (bank[k+2], 8),(bank[k-2], 16) , (bank[k+7], -4)],
			[(bank[k+14], 8),(bank[k+10], 16), (bank[k+7], 8),(bank[k+4], 16),(bank[k+12], -4)],
			[(bank[k+17], 8),(bank[k+14], 16),(bank[k+10], 8),(bank[k+7], 16) ,(bank[k+16], -4)]
			]


	twobeats = [[(bank[k+2], 16),(bank[k+4], 16),(bank[k+2], 16),(bank[k], -8)],
			[(bank[k+5], 16),(bank[k+7], 16),(bank[k+5], 16),(bank[k+4], -8)],
			[(bank[k+9], 16),(bank[k+10], 16),(bank[k+9], 16),(bank[k+7], -8)],

			[(bank[k+2], 8),(bank[k-1], 16) , (bank[k], -8)],
			[(bank[k+5], 8), (bank[k+3], 16) , (bank[k+4], -8)],
			[(bank[k+9], 8), (bank[k+6], 16),(bank[k+7], -8)],
			[(bank[k+14], 8),(bank[k+11], 16) , (bank[k+12], -8)]
			]

	eighth = copy.deepcopy (fourbeats)
	for phrase in eighth :
		phrase.pop()

	onebeat = copy.deepcopy (twobeats)
	for phrase in onebeat :
		phrase.pop()

	allbeats = fourbeats + twobeats + eighth + onebeat
	print (allbeats)

	n = []
	b = 0
	def choose_phrase () :
	while b < 16 :
		if b == 14 :
			phrase = random.choice (twobeats)
		elif b == 13 :
			phrase = random.choice (onebeat)
		elif b == 12 :
			phrase = random.choice (fourbeats)
		else: 
			phrase = random.choice (allbeats)
		n.append (phrase)
		if phrase in twobeats:
			b = b + 2
		elif phrase in eighth :
			b = b + 2
		elif phrase in onebeat:
			b = b + 1
		else :
			b = b + 4

	notes = []

	for phrase in n:
	   for note in phrase:
	      notes.append(note)
	return notes
	#takes of the brackets so that pysynth could process it as one phrase.


def randblues () :
	blue = ['c','eb','f','f#','g','bb','c5','eb5','f5','f#5','g5']

	notes = [(random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), -4), (random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), 8), (random.choice (blue), 16), (random.choice (blue), 8), (random.choice (blue), 16),(random.choice (blue), 8), (random.choice (blue), 16), ('c', -4)]
	return notes

def playaudio (notes) :

	file = "bebop.wav"
	ps.make_wav(notes, fn = file)
	wave_obj = sa.WaveObject.from_wave_file(file)
	play_obj = wave_obj.play()
	play_obj.wait_done()

playaudio(bebop())
#bebop ()