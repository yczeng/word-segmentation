''' This files preprocesses the data. '''

def removesStressPhonemes(speech):
	'''
	Removes stress and phoneme markers. 
	Stress markers are '0-9', and primary stress markers are '1'
	'''
	result = ""
	for line in speech:
		#removes stress and phonemes
		result += line.replace("1", "").replace("0", "").replace("P", "").replace("\n", "")
	return result

def splitByUtterance(speech, noWord=False):
	'''
	Creates an array of utterances.
	If no word (to form training data), removes word boundaries.
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
	listOfUtterances = splitByUtterance(speech)
	print(listOfUtterances)

	for eachUtterance in listOfUtterances:
		# rempves empty strings
		tmpList = list(filter(None, eachUtterance.split("W")))
		
		result.append(tmpList)

		# to return average length of utterances
		totalLen += len(tmpList)
		count += 1

	return result, totalLen / count

if __name__ == '__main__':
	speech_input = 'data/mother.speech.txt'
	with open(speech_input, "r") as speech:
		noStressSpeech = removesStressPhonemes(speech)
		processedSpeech, avgLen = splitByWords(noStressSpeech)

		## To generate statistics
		# print(len(processedSpeech))
		# print(avgLen)

		# with open('data/splitByWords.txt','a') as new_speech:
		# 	new_speech.write(str(processedSpeech))

		# saveListOfUtterances = splitByUtterance(noStressSpeech, True)
		# with open('data/splitByUtterance.txt','a') as new_speech:
		# 	new_speech.write(str(saveListOfUtterances))