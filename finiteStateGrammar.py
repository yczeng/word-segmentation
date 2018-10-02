''' Goal: to create a visual of mother's speech's finite state grammar'''

def finiteStateGrammar(utteranceArray):
	'''
	Scans every syllable against syllable in memory. If the same, add to lexicon with weight.

	Args:
		utteranceArray: an array of String utterances
	Returns:
		

	'''

	probabilities = {}
	for count, eachUtterance in enumerate(utteranceArray):
		utterance = list(filter(None, eachUtterance.split("S")))
		probabilities = processUtterance(utterance, probabilities)

	return probabilities

def processUtterance(utterance, probabilities):

	for i in range(2, len(utterance)):

		previousSyllable = utterance[i-1]
		currentSyllable = utterance[i]

		if previousSyllable in probabilities:
			# check if syllable already given

			if currentSyllable in probabilities[previousSyllable]:
				probabilities[previousSyllable][currentSyllable] += 1
			else:
				probabilities[previousSyllable][currentSyllable] = 1
		else:
			probabilities[previousSyllable] = {currentSyllable: 1}

	return probabilities

