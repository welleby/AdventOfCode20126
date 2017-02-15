def debug(*input):
	if DEBUG: print(input)

def format(input):
	return input.split("\n")

def getInput(fileName):
	#return input
	file = open(fileName,"r")
	result = file.read()
	file.close()
	return result