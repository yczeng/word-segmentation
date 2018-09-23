''' This files preprocesses the data. '''

def removesStressPhonemes(speech):
	'''
	Removes stress and phoneme markers. 
	Stress markers are '0-9', and primary stress markers are '1'
	'''
	result = ""
	for line in speech:
		#removes stress and phonemes
		result += line.replace("1", "").replace("0", "").replace("P", "")
	return result

def separateByWords(speech):
	'''
	Creates an array of an array of utterances separated by words.
	utterance separated by 'U', words separated by 'W'
	'''
	result = []
	listOfUtterances = speech.split("U")
	for eachUtterance in listOfUtterances:
		# rempves empty strings
		tmpList = list(filter(None, eachUtterance.split("W")))
		result.append(tmpList)
	return result

if __name__ == '__main__':
	speech_input = 'mother.speech.txt'
	with open(speech_input, "r") as speech:
		processedSpeech = separateByWords(removesStressPhonemes(speech))
		print(processedSpeech)

		with open('splitByWords.txt','a') as new_speech:
			new_speech.write(str(processedSpeech))