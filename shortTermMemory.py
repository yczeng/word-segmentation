''' tests idea of heavy computation on limited memory '''

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

	#TODO: if checkers happens three times, right now the lexicon will only say checkers twice. That's becaues the first time it was not added to the lexicon

	memory = []
	lexicon = []
	lexiconFrequency = []
	print("length of utterance array", len(utteranceArray))
	for count, eachUtterance in enumerate(utteranceArray):
		utterance = list(filter(None, eachUtterance.split("S")))
		memory, lexicon, lexiconFrequency = forEachUtterance(utterance, memory, lexicon, lexiconFrequency)

	return memory, lexicon, lexiconFrequency

def forEachUtterance(utterance, memory=[], lexicon=[], lexiconFrequency=[]):
	newWord = []

	def insertIntoLexicon(newWord):
		# Updates both lexiconFrequency and lexicon
		if len(newWord) >= 2:

			inLexicon = False
			for index, each in enumerate(lexicon):
				if newWord == each:
					lexiconFrequency[index] += 1
					inLexicon = True
					break
			
			if not(inLexicon):
				lexicon.append(newWord)
				lexiconFrequency.append(2)
				newWord = []

		return newWord


	memoryPointer = 0
	for syllable in utterance:
		if syllable not in memory:
			memory.append(syllable)
			memoryPointer = 0
			newWord = insertIntoLexicon(newWord)

		else:
			# first time this syllable has shown up
			if len(newWord) == 0:
				for i in range(len(memory)):
					if memory[i] == syllable:
						memoryPointer = i
						newWord.append(syllable)
						break;

			# check that the second syllable is same as second in memory
			elif (memory[memoryPointer + 1] == syllable):
				memoryPointer += 1
				newWord.append(syllable)

			memory.append(syllable)

	# at the end if newWord has not been added, add it
	insertIntoLexicon(newWord)
			
	return memory, lexicon, lexiconFrequency

if __name__ == '__main__':
	utteranceArray3 = ['dhowz', 'aar', 'cheh', 'kerz', 'tuw', 'cheh', 'kerz', 'yehsS']
	utteranceArray2 = ['dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS']
	utteranceArray1 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdow2SyerSsehlfS']
	utteranceArray0 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS']

	utteranceInput = 'data/splitByUtterance.txt'
	with open(utteranceInput, "r") as speech:
		for line in speech:
			utterances = line.replace(" ", "")
			utterances = utterances.replace("'", "")
			utterances = utterances.split(',')

			result = shortTermMemory(50, utterances)
			# print(result)
			print(result[1])
			print(result[2])

			with open('data/memoryFrequences.txt','a') as results:
				results.write(str(result[1]))
				results.write("\n")
				results.write(str(result[2]))

	# utteranceLengthMemory = 50
	# results = forEachUtterance(utteranceArray3)

	# result = shortTermMemory(50, utteranceArray4)
	# # print(result)
	# print(result[1])
	# print(result[2])
	