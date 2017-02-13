#!/usr/bin/python

import re

input = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb
xidbntshgqdckieib[urwkpgpqlzuroemjp]srffrwixbhqgbnfpsgkpl[uygjtjaixctjtnanuf]qdloyaplyovscng
uumyvgqczjaadkspfu[cmacsgwkvcivtsn]cpefaqmflxkfmlkp[mfsvltdmnyzxqcrrclxk]ykmjlnxxmsv
klioqytpqhkxqiriz[rjgrssrxpxozhzbc]fysfmaiblgqhkeue[bycqedeolknahiy]pdusnyfxfcgodvj
sgjjqocmmcccpem[doeofpebaahroicm]pluzqzwkdzcovxic[zmyulluzupuododuiabvykn]ylxzlyodoxnlibiy"""

DEBUG = False
#DEBUG = True

def debug(*input):
	if DEBUG: print(input)

def format(input):
	return input.split("\n")

def getInput():
	#return input
	file = open("7_input.txt","r")
	result = file.read()
	file.close()
	return result

def shift(bab):
	return bab[1]+bab[0]+bab[1]
	
def getAbas(input):
	result = []
	for inp in input : 
		for sub in range(0,len(inp)-2):
			if inp[sub] == inp[sub+2] and inp[sub] != inp[sub+1] : result.append(inp[sub:sub+3])
	return result

def supportsSSL(input):
	hypernet = re.findall(r"(?<=\[).*?(?=\])",input)
	supernet = re.split(r"\[.*?\]",input)
	babs = getAbas (hypernet)
	abas = getAbas(supernet)
	
	debug("supernet: ",supernet)
	debug("hypernet: ",hypernet)
	debug("hyper Babs: ", babs)
	debug("super Abas: ", abas)
	
	for bab in babs:
		for aba in abas:
			if shift(bab) == aba: 
				debug("Match ",aba)
				return True
	return False


inputArray = format(getInput())

result = 0
for inp in inputArray:
	if supportsSSL(inp): 
		result+=1
	
print ("Result: ",result)

