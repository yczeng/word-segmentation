''' helper functions available to import '''

import ast

def getArrayFromTextFile(filepath, lineIndex):
	'''
	returns an array from a text file's string of an array
	this only works if textfile is on one line
	'''

	with open(filepath, "r") as text:
		for index, line in enumerate(text):
			if index == lineIndex:
				return ast.literal_eval(line)

	raise Exception('Index is out of bounds, or filepath not correct.')

# def sortLexiconByFrequency(lexicon, lexiconFrequency):
# 	set{}
# 	for wordFrequency in lexiconFrequency:
