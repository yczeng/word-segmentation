''' This file preprocesses the data. '''

def removesStressPhonemes(speech):
	'''
	Removes stress and phoneme markers. 
	Stress markers are '0-9', and primary stress markers are '1'
	'''
	result = ""
	for line in speech:
		#removes stress and phonemes
		result += line.replace("1", "").replace("0", "").replace("2", "").replace("P", "").replace("\n", "")
	return result

def splitByUtterance(speech, noWord=False):
	'''
	Creates an array of utterances.
	If noword (to form training data), removes word boundaries.
	'''
	if noWord:
		speech = speech.replace("W", "")

	result = speech.split("U")
	result = list(filter(None, result))
	return result

def splitByWords(speech):
	'''
	Creates an array of an array of utterances separated by words.
	utterance separated by 'U', words separated by 'W'

	Input speech has not yet been split by utterances.
	'''
	totalLen = 0
	count = 0

	result = []
	speech = speech.replace("U", "")
	speechWords = list(filter(None, speech.split("W")))
	
	for word in speechWords:
		processedWord = list(filter(None, word.split("S")))
		if processedWord not in result:
			result.append( processedWord )

	return result

if __name__ == '__main__':
	speech_input = 'data/mother.speech.txt'
	with open(speech_input, "r") as speech:
		noStressSpeech = removesStressPhonemes(speech)
		processedSpeech = splitByWords(noStressSpeech)

		## To generate statistics
		# print(len(processedSpeech))
		# print(avgLen)

		with open('data/splitByWords.txt','a') as new_speech:
			new_speech.write(str(processedSpeech))

		# saveListOfUtterances = splitByUtterance(noStressSpeech, True)
		# with open('data/splitByUtterance.txt','a') as new_speech:
		# 	new_speech.write(str(saveListOfUtterances))