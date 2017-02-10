#!/usr/bin/python

def format(input):
	return input.split("\n")

def getInput():
	#return input
	file = open("6_input.txt","r")
	result = file.read()
	file.close()
	return result

def getCols(inputArray):
	result = dict({})
	for inp in inputArray: #For each input
		#print(inp)
		for i in range(len(inp)): #for each character
			if i not in result:
				result[i] = {}
			#print(result[i])
			if inp[i] in result[i]:
				result[i][inp[i]] += 1
			else:
				result[i][inp[i]] = 1
	return result

inputArray = format(getInput())
cols = getCols(inputArray)
result = ""
for tup in cols:
	lst = cols[tup]
	result+=sorted(lst,key=lst.get)[0]

print("Result: %s" % result)