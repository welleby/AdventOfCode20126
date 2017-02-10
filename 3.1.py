#!/usr/bin/python
import re

class Triangle:
	def __init__(self):
		self.a = 0
		self.b = 0
		self.c = 0
	def __init__(self, a,b,c):
		self.a = a
		self.b = b
		self.c = c
	def __str__(self):
		return "A: %i, B: %i, C: %i" % (self.a,self.b,self.c)
	def isValid(self):
		if(self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
			return True
		else: return False

def format(string):
	string = re.sub("[\r\n]", "", string)
	string = re.sub(" +", ",", string)
	string = re.sub("^,", "", string)
	return string

def getInput():
	file = open("3.1_input.txt","r")
	result = file.read()
	file.close()
	result = format(result)
	return result


intArray = getInput().split(",")
if len(intArray) % 3 !=0:
	raise IOError("Input Not evenly devideble with 3")

triangles = []
for i in range(0,len(intArray),3):
	triangles.append(Triangle(int(intArray[i]),int(intArray[i+1]),int(intArray[i+2])))

valid = 0
invalid = 0
for triangle in triangles:
	if(triangle.isValid()):
		valid+=1
	else:
		invalid+=1
print ("Valid: "+ str(valid))
print ("Invalid: "+ str(invalid))