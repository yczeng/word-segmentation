''' main file for running stuff '''
import memory as memory

if __name__ == '__main__':
	utteranceArray3 = ['dhowz', 'aar', 'cheh', 'kerz', 'tuw', 'cheh', 'kerz', 'yehsS']
	utteranceArray2 = ['dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS']
	utteranceArray1 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdow2SyerSsehlfS']
	utteranceArray0 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'wehrShhaevSyuwSsiynSahShhaetSlaykSdhaetS', 'wehrSaarSyuwSgowihngS']

	utteranceArray4 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdowSyerSsehlfS', 'ahStehSrahSbliySsmaolShhaorsSfaorSyuwStuwSraydS', 'waySyuwSluhkSaetSsahmSahvSdhahStoyzSihnSdhahSbaeSskahtS', 'waantStuwS', 'duwSyuwSwaantStuwSsiySwahtSayShhaevS', 'wahtSihzSdhaetS', 'naatSihnSyaorSmawthS', 'lehtSmiySpuhtSdhehmStahSgehSdherS', 'puhtSflaorS', 'hhihzSpehnSsahlS', 'naatSdaeSdiySkowSlihnS', 'aySthihngkSperShhaepsSgowihngSbaekStuwSskuwlS', 'naatSaanSdhahSwihnSdowSsihlSaeSdahmS', 'yuwSraytSaanSdhahSpeySperS', 'maySpeySperS', 'serSkahsS', 'sihStihngSihnSaeSdahmzSchehrS', 'waySyuwSrehdSihtStuwSmiyS', 'daogS', 'kaeSthiyS', 'hhaornS', 'ihzSdhihsSahShhaornS', 'hhawSmehSniySduwSyuwShhaevSlaykSdhihsS', 'wehrSaarSyuwSgowihngS', 'hhawSdahzSahSbahSniySraeSbahtSwaokS', 'dahzShhiySwaokSlaykSyuwSaorSdahzShhiySgowShhaapShhaapShhaapS', 'wahtSaarSyuwSduwihngS', 'swiypSbruwmS', 'ihzSdhaetSahSbruwmS', 'aySthaotSihtSwaazSahSbrahshS', 'owSkeyS', 'aeSdahmSsmihthS', 'ihzSdhaetSdhahSbahSniySraeSbahtsSneymS', 'gehtSwahtS', 'wahtS', 'wahtSihzSihtS', 'hhihrSahStraekSterS', 'nowSaySthihngkSahStrahkS', 'ihfSyuwSluhkSawtSdhahSahSdherSwihnSdowSmeySbiySsiySihtS', 'dihdSyuwSsiySdhahStrahkS', 'yuwSsiySihtS', 'dhehrSgowzSwahnS', 'dhehrSgowzSwahnS', 'puhtSdhahStrahkSwehrS', 'aySthihngkSdhaetSwahnzStuwSlaarjhStuwSgowSihnSdhahSwihnSdowS', 'towStrahkSkahmShhihrS', 'wehrS', 'ahSbihgStrahkS', 'dhehrSgowzSahSnahSdherSwahnS', 'bihSziySbuhlSdowSzerS', 'luhkSahSnahSdherSwahnS', 'bowSzowS', 'dihdSyuwSshowSerSsahSlahSdhaetS', 'duwSyuwSnowSwahtSdhowzSaarS', 'aySgehsSshiySmaytSlaykStuwSsiySdhaetS', 'wahtSkayndSahvShhaetSihzSdhaetS', 'aeSdahmzShhaetS', 'wehrShhaevSyuwSsiynSahShhaetSlaykSdhaetS']

	utteranceInput = 'data/splitByUtterance.txt'
	# with open(utteranceInput, "r") as speech:
	# 	for line in speech:
	# 		utterances = line.replace(" ", "")
	# 		utterances = utterances.replace("'", "")
	# 		utterances = utterances.split(',')

	# 		result = memory.shortTermMemory(50, utterances)
	# 		# print(result)
	# 		print(result[0])
	# 		print(result[1])
	# 		print(result[2])

	# 		with open('data/memoryFrequences.txt','a') as results:
	# 			results.write(str(result[1]))
	# 			results.write("\n")
	# 			results.write(str(result[2]))

	# utteranceLengthMemory = 50
	# results = forEachUtterance(utteranceArray3)

	memory, lexicon, lexiconFrequency = memory.shortTermMemory(50, utteranceArray0)
	print(memory)
	print(lexicon)
	print(lexiconFrequency)