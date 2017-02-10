#!/usr/bin/python
import re
from collections import defaultdict

rowPattern = re.compile(r'(.*?)(\d+)\[(.*)\]')
valid1 = "not-a-real-room-404[oarel]"
valid2 = "aaaaa-bbb-z-y-x-123[abxyz]"
valid3 = "a-b-c-d-e-f-g-h-987[abcde]"
invalid1 = "totally-real-room-200[decoy]"


def isValid(input, checkSum):
	dict = defaultdict(int)
	for letter in input:
		dict[letter]+=1
	
	sortedActual = []
	for w in sorted(dict, key=dict.get, reverse=True):
		sortedActual.append((w,dict[w]))
	commonValues = defaultdict(int)
	for com in checkSum:
		commonValues[com] = dict[com]
	
	i = 0
	for com in sorted(commonValues, key=commonValues.get, reverse=True):
		if(commonValues[com]!=sortedActual[i][1]):
			return False
		i+=1
	return True
	
def rowInfo(string):
	letters = rowPattern.sub(r'\1',string)
	letters = letters.replace("-","")
	digits = int(rowPattern.sub(r'\2',string))
	common = rowPattern.sub(r'\3',string)
	valid = isValid(letters,common)
	return digits,valid

def getInput():
	file = open("4.1_input.txt","r")
	result = file.read()
	file.close()
	return result


inputArray = getInput().split("\n")

sum = 0
#inputArray = [valid1,valid2,valid3,invalid1]
for input in inputArray:
	digits, valid = rowInfo(input)
	print(digits,valid)
	if valid: 
		sum+=digits

print(sum)




#print ("Valid: "+ str(valid))
#print ("Invalid: "+ str(invalid))
