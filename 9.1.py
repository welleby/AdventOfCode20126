#!/usr/bin/python
from helper import *
import re


#input = "X(8x2)(3x3)ABCY(1x1)A"
#input = "(22x11)(3x5)ICQ(9x5)IYUPTHPKX(28x2)(41x6)(16x9)SIUZCKMFZFXKUYTQ"
input = getInput("9_input.txt")

DEBUG = False
#DEBUG = True

#inputArray = format(getInput("9_input.txt"))
i=0
result = ""
#print(input)
while i < len(input):
	srch = re.search(r"^(.*?)(?=\(|$)",input[i:])
	#print("F: ",input[i:])
	if(srch.group()!=''):
		result+=srch.group()
		i+=srch.end()
		#print("O: ",input[i:])
	else:
		srch = re.search(r'^\((\d+)x(\d+)\)',input[i:])
		chars,repeat =srch.groups()
		idx = srch.end()
		chars = int(chars)
		repeat = int(repeat)
		result+=(input[i+idx:i+idx+chars] * repeat)
		i+=idx+chars

print("Result :", len(result))
