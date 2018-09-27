''' tests idea of heavy computation on limited memory '''

#TODO: arrange lexicon by highest frequency first

def shortTermMemory(memoryLength, utteranceArray):
	'''
	Scans every syllable against syllable in memory. If the same, add to lexicon with weight.

	Args:
		utteranceArray: an array of String utterances
		memoryLength: an int for memory length
	Returns:
		Memory: list of utterances (which is a list of syllables)
		Lexicon: list of words that have been segmented

	'''
	memory = []
	lexicon = []
	lexiconFrequency = []
	print("length of utterance array", len(utteranceArray))
	for count, eachUtterance in enumerate(utteranceArray):
		utterance = list(filter(None, eachUtterance.split("S")))
		memory, lexicon, lexiconFrequency = forEachUtterance(utterance, memory, lexicon, lexiconFrequency)

	return memory, lexicon, lexiconFrequency

def checkInMemory(memory, syllable):
	''' checks memory for syllable '''
	for memUttIndex, memoryUtterance in enumerate(memory):
		for memSyllIndex, memorySyllable in enumerate(memoryUtterance):
			if memorySyllable == syllable:

				return True, memUttIndex, memSyllIndex

	return False, None, None

def insertIntoLexicon(newWord, lexicon, lexiconFrequency):
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

def forEachUtterance(utterance, memory=[], lexicon=[], lexiconFrequency=[]):
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

	#TODO: if the word matches with a one syllable word in memory, it doesn't try to match more words in a latter part of memory...
	# maybe that's a good time to segment it?

	# Adds monosyllabic words to lexicon
	if len(utterance) == 1:
		memory.append(utterance)
		newWord, lexicon, lexiconFrequency = insertIntoLexicon(utterance[0], lexicon, lexiconFrequency)
		return memory, lexicon, lexiconFrequency

	memUttPointer = 0
	memSyllPointer = 0
	tmpMemory = []
	newWord = []
	isInMiddleOfSyllable = False
	for syllable in utterance:
		
		if isInMiddleOfSyllable:
			inMemory = memory[memUttPointer][memSyllPointer] == syllable
		else:
			# check if syllable is in memory, stores location
			checkMemoryResults = checkInMemory(memory, syllable)
			inMemory = checkMemoryResults[0]

			if len(newWord) == 0:
				memUttPointer = checkMemoryResults[1]
				memSyllPointer = checkMemoryResults[2]

		if not(inMemory):
			tmpMemory.append(syllable)
			memUttPointer = 0
			memSyllPointer = 0
			# this also resets newWord to []
			newWord, lexicon, lexiconFrequency = insertIntoLexicon(newWord, lexicon, lexiconFrequency)
			inMemory = False
		else:
			if (len(memory[memUttPointer]) - 1) > memSyllPointer:
				memSyllPointer += 1
				isInMiddleOfSyllable = True
			else:
				isInMiddleOfSyllable = False
				newWord, lexicon, lexiconFrequency = insertIntoLexicon(newWord, lexicon, lexiconFrequency)

			newWord.append(syllable)
			tmpMemory.append(syllable)

	# at the end if newWord has not been added, add it
	newWord, lexicon, lexiconFrequency = insertIntoLexicon(newWord, lexicon, lexiconFrequency)
	memory.append(tmpMemory)
			
	return memory, lexicon, lexiconFrequency

def rearranageByHighestFrequency(lexicon, lexiconFrequency):
	pass