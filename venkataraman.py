''' Implements dynamic search algorithm from Venkataraman '''

import math

# lexicon is a dictionary of tuples where tuples are phonemes representing words and the values represent frequency
lexicon = {}

# this is probably just strings as keys and frequencies as values
phonemes = {'I': 0,'E': 0,'&': 0,'A': 0,'a': 0,'O': 0,'U': 0,'6': 0,'i': 0,'e': 0,'9': 0,'Q': 0,'u': 0,'o': 0,'7': 0,'3': 0,'R': 0,'#': 0,'%': 0,'*': 0,'(': 0,')': 0,'p': 0,'b': 0,'m': 0,'t': 0,'d': 0,'n': 0,'k': 0,'g': 0,'N': 0,'f': 0,'v': 0,'T': 0,'D': 0,'s': 0,'z': 0,'S': 0,'Z': 0,'h': 0,'c': 0,'G': 0,'l': 0,'r': 0,'L': 0,'~': 0,'M': 0,'y': 0,'w': 0,'W': 0}

def evalUtterance(utterance):
	n = len(utterance)

	best_segment = n
	bestCost = evalWord(tuple(utterance[0:n]))
	bestSegpoint = 0
	for i in range(n):
		subUtterance = utterance[0:i]
		word = utterance[i::]
		cost = evalUtterance(subUtterance) + evalWord(tuple(word))
		if cost < bestCost:
			bestCost = cost
			bestSegpoint = i

	insertWordBoundary(utterance, bestSegpoint)
	return bestCost

def insertWordBoundary(utterance, bestSegpoint):
	# for inserting into word boundary
	tupleWord = tuple(utterance[bestSegpoint::])
	if tupleWord in lexicon:
		lexicon[tupleWord] += 1
	else:
		lexicon[tupleWord] = 1

	for phoneme in tupleWord:
		if phoneme in phonemes:
			phonemes[phoneme] += 1
		else:
			phonemes[phonemes] = 0


def evalWord(word):
	'''
	Calculates a log score for word

	Args:
		word: word w[0..k] where w[i] are the phonemes in it. Word is a TUPLE
	Returns:

	'''
	score = 0
	# implement lexicon with words and give frequencies. Maybe a dictionary
	if word not in lexicon:

		if len(lexicon) == 0:
			escape = 0
		else:
			escape = len(lexicon) / len(lexicon) + sum(lexicon.values())

		P_0 = phonemes['#']

		if escape == 0 and P_0 == 0:
			score = 0
		else:
			try:
				score = - math.log(escape) - math.log(P_0 / (1-P_0))
			except:
				print(escape)
				print(P_0 / 1-P_0)
				print(lexicon)
				exit()

		if len(phonemes) != 0:
			for i in range(len(word)):
				score -= math.log(phonemes[word[i]])

	else:
		P_W = lexicon[word] / (len(lexicon) + sum(lexicon.values()))
		score = - math.log(P_W)
	return score

if __name__ == "__main__":
	with open('Bernstein-Ratner87', "r") as text:
		for line in text:
			processedLine = line.replace('\n', '').replace(" ", "")
			print(processedLine)
			evalUtterance(processedLine)
