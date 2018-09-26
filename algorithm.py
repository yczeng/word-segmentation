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
	newWord = []

	memoryPointer = 0
	for syllable in utteranceArray:

		if syllable not in memory:
			memory.append(syllable)
			memoryPointer = 0
			if len(newWord) >= 2:
				lexicon.append(newWord)
				newWord = []
		else:
			if len(newWord) == 0:
				for i in range(len(memory)):
					if memory[i] == syllable:
						memoryPointer = i
						newWord.append(syllable)
						print("memoryPointer is", memoryPointer)
			
			
			elif (memory[memoryPointer + 1] == syllable):

				memoryPointer += 1
				newWord.append(syllable)

			memory.append(syllable)

	if len(newWord) >= 2:
		lexicon.append(newWord)
		newWord = []
			
	return memory, lexicon



if __name__ == '__main__':
	utteranceArray3 = ['dhowz', 'aar', 'cheh', 'kerz', 'tuw', 'cheh', 'kerz', 'yehsS']

	utteranceArray2 = ['dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS']
	utteranceArray1 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdow2SyerSsehlfS']
	
	utteranceLengthMemory = 50
	results = shortTermMemory(50, utteranceArray3)
	print(results)