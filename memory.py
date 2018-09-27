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

	def insertIntoLexicon(newWord):
		'''
		if len of newWord is >=2, then it adds it to the lexicon.
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

		return newWord

	# Adds monosyllabic words to lexicon
	if len(utterance) == 1:
		memory.append(utterance)
		insertIntoLexicon(utterance[0])
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
			inMemory = False
			for memUttIndex, memoryUtterance in enumerate(memory):
				for memSyllIndex, memorySyllable in enumerate(memoryUtterance):
					if memorySyllable == syllable:
						inMemory = True
						# don't save these pointers unless it's the first time
						# you want to use the old memory pointers
						if len(newWord) == 0:
							memUttPointer = memUttIndex
							memSyllPointer = memSyllIndex
						break
				if inMemory:
					break
		
		if not(inMemory):
			tmpMemory.append(syllable)
			memUttPointer = 0
			memSyllPointer = 0
			# this also resets newWord to []
			newWord = insertIntoLexicon(newWord)
			inMemory = False
		else:
			# first time this syllable has shown up
			if len(newWord) == 0:
				newWord.append(syllable)
				memSyllPointer += 1
				isInMiddleOfSyllable = True

			# check that the second syllable is same as second in memory
			elif (len(memory[memUttPointer]) - 1) > memSyllPointer:
				memSyllPointer += 1
				newWord.append(syllable)
				isInMiddleOfSyllable = True

			# has reached the end
			else:
				newWord.append(syllable)

			tmpMemory.append(syllable)

	# at the end if newWord has not been added, add it
	insertIntoLexicon(newWord)
	memory.append(tmpMemory)
			
	return memory, lexicon, lexiconFrequency

def rearranageByHighestFrequency(lexicon, lexiconFrequency):
	pass