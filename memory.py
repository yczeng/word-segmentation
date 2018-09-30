''' tests idea of heavy computation on limited memory '''

#TODO: arrange lexicon by highest frequency first
#TODO: if the word matches with a one syllable word in memory, it doesn't try to match more words in a latter part of memory...
# maybe that's a good time to segment it?

def shortTermMemory(memoryLength, utteranceArray, monosyllabicIsWord=False):
	'''
	Scans every syllable against syllable in memory. If the same, add to lexicon with weight.

	Args:
		utteranceArray: an array of String utterances
		memoryLength: an int for memory length
	Returns:
		memory: list of utterances (which is a list of syllables)
		lexicon: a list of segmentations, either strings or lists of syllables
		lexiconFrequency: a list of segmentations frequency

	'''
	memory = []
	lexicon = []
	lexiconFrequency = []

	for count, eachUtterance in enumerate(utteranceArray):
		utterance = list(filter(None, eachUtterance.split("S")))
		memory, lexicon, lexiconFrequency = forEachUtterance(utterance, memory, lexicon, lexiconFrequency)

	return memory, lexicon, lexiconFrequency

def checkInMemory(memory, syllable):
	'''
	checks memory for syllable
	returns an array of memory locations
	'''

	# an array of a set of tuples representing memory location
	results = []
	for memUttIndex, memoryUtterance in enumerate(memory):
		for memSyllIndex, memorySyllable in enumerate(memoryUtterance):
			if memorySyllable == syllable:
				results.append( (memUttIndex, memSyllIndex) )

	return results

def tryInsertIntoLexicon(newWord, lexicon, lexiconFrequency):
	'''
	if len of newWord is >=2 or is monsyllabic, then it adds it to the lexicon.
	otherwise it resets newWord to []
	'''

	if len(newWord) >= 2 or isinstance(newWord, str):
		inLexicon = False

		# if word already in lexicon, increase frequency
		for index, each in enumerate(lexicon):
			if newWord == each:
				lexiconFrequency[index] += 1
				inLexicon = True
				break
		
		if not(inLexicon):
			lexicon.append(newWord)
			if (isinstance(newWord, str)):
				lexiconFrequency.append(1)
			else:
				# accounts for first time word showed up and matched word				
				lexiconFrequency.append(2)
	
	newWord = []

	return newWord, lexicon, lexiconFrequency

def forEachUtterance(utterance, memory=[], lexicon=[], lexiconFrequency=[], monosyllabicIsWord=False):
	'''
	This is a helper function for shortTermMemory

	Args:
		utterance: an array of Syllable strings
		memory: a list utterances, which are lists of syllables
		lexicon: a list of segmentations, either strings or lists of syllables
		lexiconFrequency: a list of segmentations frequency
	Returns:
		memory: a list utterances, which are lists of syllables
		lexicon: a list of segmentations, either strings or lists of syllables
		lexiconFrequency: a list of segmentations frequency
	'''

	if monosyllabicIsWord:
		# Adds monosyllabic words to lexicon
		if len(utterance) == 1:
			memory.append(utterance)
			newWord, lexicon, lexiconFrequency = tryInsertIntoLexicon(utterance[0], lexicon, lexiconFrequency)
			return memory, lexicon, lexiconFrequency

	memUttPointer = 0
	memSyllPointer = 0
	newWord = []
	isInMiddleOfWord = False
	for syllable in utterance:
		
		if isInMiddleOfWord:
			inMemory = memory[memUttPointer][memSyllPointer] == syllable
		else:
			# check if syllable is in memory, stores locations
			# checkInMemory returns a tuple of locations. Check all of them.
			checkMemoryResults = checkInMemory(memory, syllable)
			inMemory = len(checkMemoryResults) != 0				

		if not(inMemory):
			memUttPointer = 0
			memSyllPointer = 0
			# this also resets newWord to []
			newWord, lexicon, lexiconFrequency = tryInsertIntoLexicon(newWord, lexicon, lexiconFrequency)
		else:
			memUttPointer = checkMemoryResults[0][0]
			memSyllPointer = checkMemoryResults[0][1]
				# TODO: here I want to run it for every occurance. CHECK ALL OUTPUTS OF CHECK MEMORY

			newWord.append(syllable)

			# checks if the word has ended (is the syllable the last in the utterance)
			if (len(memory[memUttPointer]) - 1) > memSyllPointer:
				memSyllPointer += 1
				isInMiddleOfWord = True

			else:
				newWord, lexicon, lexiconFrequency = tryInsertIntoLexicon(newWord, lexicon, lexiconFrequency)
				print("LEXICON", lexicon)
				isInMiddleOfWord = False


	# at the end if newWord has not been added, add it
	newWord, lexicon, lexiconFrequency = tryInsertIntoLexicon(newWord, lexicon, lexiconFrequency)
	memory.append(utterance)
			
	return memory, lexicon, lexiconFrequency