#Kaki Su
#February 22, 2019
#We recommend using a white background for the terminal so that the colors come out nicely. We also recommend using two earbuds (as opposed to just one ear) so that you 
#This program generates jazz improvisation on the bebop scale. You can enter the chords you want, and it would generate the chords on the 
#I have neither given nor received unauthorized aid. Jiaqi Su
#playing audio with python: https://stackoverflow.com/questions/260738/play-audio-with-python/34179010
#finding the index of an item: https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python
#taking out value from tuple: https://stackoverflow.com/questions/11458239/python-changing-value-in-a-tuple
#merging list: https://stackoverflow.com/questions/1720421/how-to-concatenate-two-lists-in-python
#mixing wav files: https://stackoverflow.com/questions/4039158/mixing-two-audio-files-together-with-python

import pysynth_b as ps
import simpleaudio as sa
import random
import sys
import copy
import os
import time
import numpy
from pydub import AudioSegment

#the range of pitch that will be used to improvise, from low to high. 
bank = ["c3", "c#3", "d3", "d#3", "e3", "f3", "f#3", "g3", "g#3", "a3", "a#3", "b3", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b", "c5", "c#5", "d5", "d#5", "e5", "f5", "f#5", "g5", "g#5", "a5", "a#5", "b5", "c6", "c#6", "d6", "d#6", "e6", "f6", "f#6", "g6", "g#6", "a6", "a#6", "b6"]


#function that returns the index of the note in the bank. used to determine the interval between notes
def return_interval (note) :
	lst = list(note)
	return int(bank.index(lst[0]))

#function to clear the terminal
def clear():  
	os.system('clear')
	print ("\n")

#function that pauses a little between each letter so that it makes the sentences look like it's being typed out.
def delay_print(s): 
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

#would pause function for two seconds
def pause ():
	time.sleep(2)


def main () :

	notes = []
	c1 = []
	c2 = []
	c3 = []
	c4 = []

	#algorithm that generates the bebop scale
	def gen_bebop (k, beat) :
		#This function will improvise based on set bebop scale and common patterns.
		#k = 12 will be c major, k = 13 will be c# major, k = 14 will be d major, and so on.

		#these are the patterns are commonly used patterns/phrases during improvisation. They are organized depending on how many beats they take up.
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
				[(bank[k+17], 8),(bank[k+14], 16),(bank[k+10], 8),(bank[k+7], 16) ,(bank[k+16], -4)],

				[(bank[k+19], 8),(bank[k+17], 16),(bank[k+16], 8),(bank[k+14], 16) ,(bank[k+12], -4)],
				[(bank[k+12], 8),(bank[k+11], 16),(bank[k+10], 8),(bank[k+9], 16) ,(bank[k+7], -4)],
				[(bank[k+10], 8),(bank[k+9], 16),(bank[k+7], 8),(bank[k+5], 16) ,(bank[k+4], -4)],
				[(bank[k+7], 8),(bank[k+5], 16),(bank[k+4], 8),(bank[k+2], 16) ,(bank[k], -4)],
				[(bank[k+19], 8),(bank[k+17], 16),(bank[k+16], 8),(bank[k+14], 16) ,(bank[k+12], -4)],
				[(bank[k+12], 8),(bank[k+11], 16),(bank[k+10], 8),(bank[k+9], 16) ,(bank[k+7], -4)],
				[(bank[k+10], 8),(bank[k+9], 16),(bank[k+7], 8),(bank[k+5], 16) ,(bank[k+4], -4)],
				[(bank[k+7], 8),(bank[k+5], 16),(bank[k+4], 8),(bank[k+2], 16) ,(bank[k], -4)]

				]

		twobeats = [[(bank[k+2], 16),(bank[k+4], 16),(bank[k+2], 16),(bank[k], -8)],
				[(bank[k+5], 16),(bank[k+7], 16),(bank[k+5], 16),(bank[k+4], -8)],
				[(bank[k+9], 16),(bank[k+10], 16),(bank[k+9], 16),(bank[k+7], -8)],
				[(bank[k+14], 16),(bank[k+16], 16),(bank[k+14], 16),(bank[k+12], -8)],
				[(bank[k+17], 16),(bank[k+19], 16),(bank[k+17], 16),(bank[k+15], -8)],

				[(bank[k+5], 8), (bank[k+3], 16) , (bank[k+4], -8)],
				[(bank[k+9], 8), (bank[k+6], 16),(bank[k+7], -8)],
				[(bank[k+14], 8),(bank[k+11], 16) , (bank[k+12], -8)],
				[(bank[k+17], 8), (bank[k+15], 16) , (bank[k+16], -8)]

				]

		#the two new lists here eliminates the last note from the above two lists.

		eighth = copy.deepcopy (fourbeats)
		for phrase in eighth :
			phrase.pop()

		onebeat = copy.deepcopy (twobeats)
		for phrase in onebeat :
			phrase.pop()

		#combination of all patterns
		allbeats = fourbeats + twobeats + eighth + onebeat

		#below are the rules that would make up the phrases
		n = []
		a = 0
		b = 0
		while b < beat :

			#picks the phrase based on how many more beats you have to fill
			if len(c1) == totalmeasures - 1 :
				phrase = random.choice (fourbeats)
				#will select from fourbeats for the last phrase so that it sounds conclusive
			else : 
				if b == (beat - 1) :
					phrase = random.choice (onebeat)
				elif b == beat -2 or b == beat - 3 :
					phrase = random.choice (onebeat + eighth + twobeats)
				else:
					phrase = random.choice (allbeats)

			#limits the interval between key changes less than 4 half steps so that it sounds natural

			if len (n) == 0 :
				if len(notes) != 0 :
					if a < 30 :
						if ((return_interval (phrase[0]) + 3 >= return_interval(notes[-1])) and (return_interval (phrase[0]) - 3 <= return_interval(notes[-1]))):
							n.append (phrase)
							if phrase in twobeats:
								b = b + 2
							elif phrase in eighth:
								b = b + 2
							elif phrase in onebeat:
								b = b + 1
							else :
								b = b + 4

						else :
							a = a + 1
					#if they couldn't find one that is within 3 intervals after 30 tries, it will expand the range
					elif ((return_interval (phrase[0]) + 10 >= return_interval(notes[-1])) and (return_interval (phrase[0]) - 10 <= return_interval(notes[-1]))):
						n.append (phrase)
						if phrase in twobeats:
							b = b + 2
						elif phrase in eighth:
							b = b + 2
						elif phrase in onebeat:
							b = b + 1
						else :
							b = b + 4
					else :
						pass

				else: 
					n.append (phrase)
					if phrase in twobeats:
						b = b + 2
					elif phrase in eighth:
						b = b + 2
					elif phrase in onebeat:
						b = b + 1
					else :
						b = b + 4

			#limits the interval between phrases less than 2 half steps so that it sounds natural
			else:
				if ((return_interval (phrase[0]) + 2 >= return_interval(n[-1][-1])) and (return_interval (phrase[0]) - 2 <= return_interval(n[-1][-1]))) :
					n.append (phrase)
					if phrase in twobeats:
						b = b + 2
					elif phrase in eighth :
						b = b + 2
					elif phrase in onebeat:
						b = b + 1
					else :
						b = b + 4
				else : 
					pass

		#takes off the brackets so that pysynth could process it as one phrase.
		for phrase in n:
		   for note in phrase:
		      notes.append(note)

	#generates standard blues chord depending on the key by generating four separate notes
	def gen_chord (k) :

		note1 = (bank[k-8], -2)
		c1.append (note1)

		note2 = (bank[k-5], -2)
		c2.append (note2)

		note3 = (bank[k-2], -2)
		c3.append (note3)

		note4 = (bank[k+2], -2)
		c4.append (note4)

	#function that mixes the chord and melody together
	def mix () :

		ps.make_wav(c1, fn = "chord1.wav")
		ps.make_wav(c2, fn = "chord2.wav")
		ps.make_wav(c3, fn = "chord3.wav")
		ps.make_wav(c4, fn = "chord4.wav")
		ps.make_wav(notes, fn = "bebop.wav")

		sound1 = AudioSegment.from_file("chord1.wav")
		quieter_via_method = sound1.apply_gain(-10)
		quieter_via_operator = sound1 - 10

		sound2 = AudioSegment.from_file("chord2.wav")
		quieter_via_method = sound2.apply_gain(-10)
		quieter_via_operator = sound2 - 10

		sound3 = AudioSegment.from_file("chord3.wav")
		quieter_via_method = sound3.apply_gain(-10)
		quieter_via_operator = sound3 - 10

		sound4 = AudioSegment.from_file("chord4.wav")
		quieter_via_method = sound4.apply_gain(-10)
		quieter_via_operator = sound4 - 10

		melody = AudioSegment.from_file("bebop.wav")
		quieter_via_method = melody.apply_gain(+20)
		quieter_via_operator = melody + 20

		onetwo = sound1.overlay(sound2)
		onetwothree = onetwo.overlay(sound3)
		chord = onetwothree.overlay (sound4)
		combined = chord.overlay(melody)

		combined.export("combined.wav", format='wav')

	#function that reads the generated wav file and plays the audio in the terminal
	def playaudio (file) :
		wave_obj = sa.WaveObject.from_wave_file(file)
		play_obj = wave_obj.play()
		play_obj.wait_done()

	#---------below is the code for terminal display------------

	#shows the current score so that the user can keep track of their entered chords
	def show_score (totallines) :
		clear()
		print ("\u001b[31mEnter a chord and press enter. Each chord you enter will equal a measure.\u001b[0m")
		print ("\u001b[33m* Enter 'show' to see what chords you can enter.\u001b[0m")
		print ("\u001b[33m* Enter 'quit' to exit.\u001b[0m")
		print ("--------------------\n")
		for y in range (totallines) :
			for x in range (4) :
				print (l[x][y], end="    ")
			print ("\n") 
		print ("--------------------")

	def action() :
		show_score(totallines)
		chord = input ("Chord?: ")

		#matches the entered key with the right k values which determines the key for the generate_ functions
		if str.lower(chord) == "c" :
			l[x][y] = "C "
			gen_bebop(12, 4)
			gen_chord(12)

		elif str.lower(chord) == "c#" :
			l[x][y] = "C#"
			gen_bebop(13, 4)
			gen_chord(13)

		elif str.lower(chord) == "db":
			l[x][y] = "Db"
			gen_bebop(13, 4)
			gen_chord(13)

		elif str.lower(chord) == "d" :
			l[x][y] = "D "
			gen_bebop(14, 4)
			gen_chord(14)

		elif str.lower(chord) == "d#" :
			l[x][y] = "D#"
			gen_bebop(15, 4)
			gen_chord(15)

		elif str.lower(chord) == "eb":
			l[x][y] = "Eb"
			gen_bebop(15, 4)
			gen_chord(15)

		elif str.lower(chord) == "e" :
			l[x][y] = "E "
			gen_bebop(16, 4)
			gen_chord(16)

		elif str.lower(chord) == "f" :
			l[x][y] = "F "
			gen_bebop(17, 4)
			gen_chord(17)

		elif str.lower(chord) == "f#" :
			l[x][y] = "F#"
			gen_bebop(18, 4)
			gen_chord(18)

		elif str.lower(chord) == "gb":
			l[x][y] = "Gb"
			gen_bebop(18, 4)
			gen_chord(18)

		elif str.lower(chord) == "g" :
			l[x][y] = "G "
			gen_bebop(7, 4)
			gen_chord(7)

		elif str.lower(chord) == "g#" :
			l[x][y] = "G#"
			gen_bebop(8, 4)
			gen_chord(8)

		elif str.lower(chord) == "ab":
			l[x][y] = "Ab"
			gen_bebop(8, 4)
			gen_chord(8)

		elif str.lower(chord) == "a" :
			l[x][y] = "A "
			gen_bebop(9, 4)
			gen_chord(9)

		elif str.lower(chord) == "a#" :
			l[x][y] = "A#"
			gen_bebop(10, 4)
			gen_chord(10)

		elif str.lower(chord) == "bb":
			l[x][y] = "Bb"
			gen_bebop(10, 4)
			gen_chord(10)

		elif str.lower(chord) == "b" :
			l[x][y] = "B "
			gen_bebop(11, 4)
			gen_chord(11)

		elif str.lower(chord) == "show" :
			print ("\nHere is the list of chords you can enter: \n[C, C#, D, D#, Eb, E, F, F#, Gb, G, G#, Ab, A, A#, Bb, B]\n")
			input ("Press any key when you are done.")
			action()

		elif str.lower(chord) == "quit" :
			delay_print("Are you sure you want to quit?")
			yesorno = input ("\nEnter yes or no: ")
			if str.lower (yesorno) == "yes" :
				quit()
			elif str.lower (yesorno) == "no" :
				action()
			else: 
				delay_print ("Please enter yes or no. ")
				action()

		else :
			delay_print("Are you sure you entered a chord? Try again.")
			input (" [Press Enter]")
			action()

	#asks if the user wants to play the generated improv with or without the chords.
	def improv_or_chord () :
		delay_print ("\nDo you want to hear the improvisation alone or with chords?\n")
		improv_chord = input ("Enter 'alone' or 'chord': ")
		if str.lower(improv_chord) == "alone" :
			ps.make_wav(notes, fn = "bebop.wav")
			playaudio("bebop.wav")
		elif str.lower (improv_chord) == "chord" :
			mix()
			playaudio("combined.wav")
		else: 
			delay_print ("Are you sure you entered a right command?\n")
			improv_or_chord ()

	#asks if the user wants to listen to the improvisation again
	def playagain () :
		clear()
		delay_print ("Would you like to listen to the improvisation again?")
		yesorno = input ("\nEnter yes or no: ")
		if str.lower (yesorno) == "yes" :
			improv_or_chord ()
			playagain()
		elif str.lower (yesorno) == "no" :
			pass
		else: 
			delay_print ("Please enter yes or no. ")
			playagain ()

	#gives user the option to improvise again.
	def improvagain () : 
		clear()
		delay_print ("Would you like to make another improvisation?")
		yesorno = input ("\nEnter yes or no: ")
		if str.lower (yesorno) == "yes" :
			main ()
		elif str.lower (yesorno) == "no" :
			delay_print ("Bye! Hope you had fun!  \n\n")
			quit()
		else: 
			delay_print ("Please enter yes or no. ")
			improvagain ()

#here starts the main function

	delay_print ("\nHow many measures do you want to improvise for? \nYou can do 4, 8, 12, or 16 measures.\n")
	try : 
		totalmeasures = int(input("\nEnter 4, 8, 12, or 16: "))
		if totalmeasures== 4 or totalmeasures == 8 or totalmeasures == 12 or totalmeasures == 16:
			clear()
			delay_print ("Sweet! We will improvise on "+str(totalmeasures)+" measures. \nNow, You will enter what chord you want for each measure.....")
			input (" [Press Enter]")
			totallines = int(totalmeasures/4)
			l = [["? "] * (totallines) for x in range (4)]
			for y in range (totallines) :
				for x in range (4) :
					show_score(totallines)
					action()
			show_score(totallines)
			improv_or_chord ()
			playagain()
			improvagain () 
		else:
			delay_print ("Are you sure you entered a right number?")
			input (" [Press Enter]")
			main()
	except ValueError : #when user enter a string or incorrect number of arguments etc
		delay_print ("Are you sure you entered a number? Try again.")
		input (" [Press Enter]")
		main ()

clear()
delay_print ("\u001b[31mW E L C O M E !\u001b[0m \n\nThis program generates jazz improvisation on the chords of your choice using the bebop scale!")
input ("  [Press Enter]")
main()


