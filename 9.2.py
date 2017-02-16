#!/usr/bin/python
from helper import *
import re


#input = "X(8x2)(3x3)ABCY(1x1)A"
#input = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
#input = "(27x12)(20x12)(13x14)(7x10)(1x12)A"

input = getInput("9_input.txt")

def getChars(input,prev=1):
	i=0
	result = 0
	while i < len(input):
		#print(input[i:], prev)
		srch = re.match(r"^(\w+?)(?=\(|$)",input[i:]) 
		#Not Compressed
		if(srch!= None and srch.group()!=''):
			length = len(srch.group())
			result+=length
			#print("\tNot compressed, adding",length)
			i+=length
		else:
			srch = re.search(r'^\((\d+)x(\d+)\)',input[i:])
			coverMore = re.match(r'^(\((\d+)x(\d+)\)){2,}',input[i:])
			chars,repeat =srch.groups()
			idx = srch.end()
			chars = int(chars)
			repeat = int(repeat)
			#print("\tCompressed: ", input[i:i+idx+chars])
			i+=idx
			if coverMore is None:
				#print("\tAdding",prev*repeat*chars)
				result+=prev*repeat*chars
				i+=chars
			else:
				#print("\tCovers more: ",input[i:i+chars])
				result+=getChars(input[i:i+chars],repeat*prev)
				i+=chars
	return result
result = getChars(input)
print("Result :", result)
