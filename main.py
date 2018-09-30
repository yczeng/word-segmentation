''' main file for running stuff '''
import memory as memory
from helpers import *
import test as test

if __name__ == '__main__':
	utteranceArray3 = ['dhowz', 'aar', 'cheh', 'kerz', 'tuw', 'cheh', 'kerz', 'yehsS']
	utteranceArray2 = ['dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS']
	utteranceArray1 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdow2SyerSsehlfS']
	utteranceArray0 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'wehrShhaevSyuwSsiynSahShhaetSlaykSdhaetS', 'wehrSaarSyuwSgowihngS', 'ahStehSrahSbliySsmaolShhaorsSfaorSyuwStuwSraydS']

	utteranceArray4 = ['bihgSdrahmS', 'hhaorsS', 'hhuwSihzSdhaetS', 'dhowzSaarSchehSkerzS', 'tuwSchehSkerzSyehsS', 'pleySchehSkerzS', 'bihgShhaornS', 'gehtSowSverSmaaSmiyS', 'shaeSdowS', 'aySlaykSihtS', 'waySyuwSrehdSshaeSdowSyerSsehlfS', 'ahStehSrahSbliySsmaolShhaorsSfaorSyuwStuwSraydS', 'waySyuwSluhkSaetSsahmSahvSdhahStoyzSihnSdhahSbaeSskahtS', 'waantStuwS', 'duwSyuwSwaantStuwSsiySwahtSayShhaevS', 'wahtSihzSdhaetS', 'naatSihnSyaorSmawthS', 'lehtSmiySpuhtSdhehmStahSgehSdherS', 'puhtSflaorS', 'hhihzSpehnSsahlS', 'naatSdaeSdiySkowSlihnS', 'aySthihngkSperShhaepsSgowihngSbaekStuwSskuwlS', 'naatSaanSdhahSwihnSdowSsihlSaeSdahmS', 'yuwSraytSaanSdhahSpeySperS', 'maySpeySperS', 'serSkahsS', 'sihStihngSihnSaeSdahmzSchehrS', 'waySyuwSrehdSihtStuwSmiyS', 'daogS', 'kaeSthiyS', 'hhaornS', 'ihzSdhihsSahShhaornS', 'hhawSmehSniySduwSyuwShhaevSlaykSdhihsS', 'wehrSaarSyuwSgowihngS', 'hhawSdahzSahSbahSniySraeSbahtSwaokS', 'dahzShhiySwaokSlaykSyuwSaorSdahzShhiySgowShhaapShhaapShhaapS', 'wahtSaarSyuwSduwihngS', 'swiypSbruwmS', 'ihzSdhaetSahSbruwmS', 'aySthaotSihtSwaazSahSbrahshS', 'owSkeyS', 'aeSdahmSsmihthS', 'ihzSdhaetSdhahSbahSniySraeSbahtsSneymS', 'gehtSwahtS', 'wahtS', 'wahtSihzSihtS', 'hhihrSahStraekSterS', 'nowSaySthihngkSahStrahkS', 'ihfSyuwSluhkSawtSdhahSahSdherSwihnSdowSmeySbiySsiySihtS', 'dihdSyuwSsiySdhahStrahkS', 'yuwSsiySihtS', 'dhehrSgowzSwahnS', 'dhehrSgowzSwahnS', 'puhtSdhahStrahkSwehrS', 'aySthihngkSdhaetSwahnzStuwSlaarjhStuwSgowSihnSdhahSwihnSdowS', 'towStrahkSkahmShhihrS', 'wehrS', 'ahSbihgStrahkS', 'dhehrSgowzSahSnahSdherSwahnS', 'bihSziySbuhlSdowSzerS', 'luhkSahSnahSdherSwahnS', 'bowSzowS', 'dihdSyuwSshowSerSsahSlahSdhaetS', 'duwSyuwSnowSwahtSdhowzSaarS', 'aySgehsSshiySmaytSlaykStuwSsiySdhaetS', 'wahtSkayndSahvShhaetSihzSdhaetS', 'aeSdahmzShhaetS', 'wehrShhaevSyuwSsiynSahShhaetSlaykSdhaetS']

	utterances = getArrayFromTextFile('data/splitByUtterance.txt', 0)

	# memory, lexicon, lexiconFrequency = memory.shortTermMemory(50, utterances)
	# # with open('data/memoryFrequencies.txt','a') as results:
	# # 	results.write(str(lexicon))
	# # 	results.write("\n")
	# # 	results.write(str(lexiconFrequency))

	# print(test.accuracy(lexicon, lexiconFrequency))
	# print(test.accuracy(lexicon, lexiconFrequency), True)
	# print(result[0])
	# print(result[1])
	# print(result[2])

	# utteranceLengthMemory = 50
	# results = forEachUtterance(utteranceArray3)

	memory, lexicon, lexiconFrequency = memory.shortTermMemory(50, utteranceArray4)
	print(memory)
	print(lexicon)
	print(lexiconFrequency)