''' Implements dynamic search algorithm from Venkataraman '''

import math

# TODO: write insertWordBoundary

def evalUtterance(utterance):
	n = len(utterance)

	best_segment = n
	bestCost = evalWord(utterance[0:n])
	for i in range(n):
		subUtterance == utterance[0:i]
		word = utterance[i::]
		cost = evalUtterance(subUtterance) + evalWord(word)
		if cost < bestCost:
			bestCost = cost
			bestSegpoint = i
	insertWordBoundary(utterance, bestSegpoint)
	return bestCost


def evalWord(word):
	'''
	Calculates a log score for word

	Args:
		word: word w[0..k] where w[i] are the phonemes in it
	Returns:

	'''
	score = 0
	# implement lexicon with words and give frequencies. Maybe a dictionary
	if L.frequency(word) == 0:
		escape = L.size() / L.size() + L.sumFrequency()
		P_0 = phonemes.relativeFrequency('#')
		score = -math.log(escape) - math.log(P_0 / (1-P_0))
		for i in range(len(word)):
			score -= log(phonemes.relativeFrequency(word[i]))
	else:
		P_W = L.frequency(w) / (L.size() + L.sumFreqencies())
		score = - math.log(P_W)
	return score
