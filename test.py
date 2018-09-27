''' various tests to summarize results '''

from helpers import *

def accuracy(lexicon, lexiconFrequency):
	'''
	Returns a list of incorrect words. Returns a list of correct words.

	Args:
		lexicon: a list of segmentations, either strings or lists of syllables
		lexiconFrequency: a list of segmentations frequency
	Returns:
		correctlySegmented: a list of correct words
		correctlySegmentedFrequency: a list of correct word frequencies
		incorrectlySegmented: a list of incorrect words
		incorrectlySegmentedFrequency: a list of correct word frequencies

	'''
	correctlySegmented = []
	correctlySegmentedFrequency = []

	incorrectlySegmented = []
	incorrectlySegmentedFrequency = []

	correctWords = getArrayFromTextFile('data/splitByWords.txt', 0)

	for index, word in enumerate(lexicon):
		if word in correctWords:
			correctlySegmented.append(word)
			correctlySegmentedFrequency.append(lexiconFrequency[index])

		else:
			incorrectlySegmented.append(word)
			incorrectlySegmentedFrequency.append(lexiconFrequency[index])

	return correctlySegmented, correctlySegmentedFrequency, incorrectlySegmented, incorrectlySegmentedFrequency
