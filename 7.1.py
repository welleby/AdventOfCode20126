#!/usr/bin/python

import re

input = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
xidbntshgqdckieib[urwkpgpqlzuroemjp]srffrwixbhqgbnfpsgkpl[uygjtjaixctjtnanuf]qdloyaplyovscng
uumyvgqczjaadkspfu[cmacsgwkvcivtsn]cpefaqmflxkfmlkp[mfsvltdmnyzxqcrrclxk]ykmjlnxxmsv
klioqytpqhkxqiriz[rjgrssrxpxozhzbc]fysfmaiblgqhkeue[bycqedeolknahiy]pdusnyfxfcgodvj
sgjjqocmmcccpem[odeofpebaahroicm]pluzqzwkdzcovxic[zmyulluzpuuiabvykn]ylxzlyooxnlibiy"""


def format(input):
	return input.split("\n")

def getInput():
	#return input
	file = open("7_input.txt","r")
	result = file.read()
	file.close()
	return result

def supportsTLS(input):
	mayNot = re.findall(r"\[.*?\]",input)
	for m in mayNot:
		if re.search(r"(?=(\w)(\w)(?!\1)(\2)(\1))",m) is not None: return False
	return re.search(r"(?=(\w)(\w)(?!\1)(\2)(\1))",input) is not None
	#return re.search(r"(?!\[.*)(\w)(\w)(?!\1)(\2)(\1)(?!\])",input) is not None and re.search(r"\[.*(\w)(\w)(?!\1)(\2)(\1).*\]",input) is None

inputArray = format(getInput())

result = 0
for inp in inputArray:
	print(inp, supportsTLS(inp))
	if supportsTLS(inp): 
		result+=1
	
print ("Result: ",result)

