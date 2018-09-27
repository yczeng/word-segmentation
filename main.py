''' main file for running stuff '''
import memory as memory

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

			result = memory.shortTermMemory(50, utterances)
			# print(result)
			print(result[0])
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