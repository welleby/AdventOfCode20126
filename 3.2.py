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

intArray0 = []
intArray1 = []
intArray2 = []

for i in range(len(intArray)):
	if int(i)%3==0: intArray0.append(int(intArray[i]))
	elif int(i)%3==1: intArray1.append(int(intArray[i]))
	elif int(i)%3==2: intArray2.append(int(intArray[i]))

print("0: %i; 1: %i; 2: %i" % (len(intArray0),len(intArray1), len(intArray2)))

triangles = []
for i in range(0,len(intArray0),3):
	triangles.append(Triangle(int(intArray0[i]),int(intArray0[i+1]),int(intArray0[i+2])))
for i in range(0,len(intArray1),3):
	triangles.append(Triangle(int(intArray1[i]),int(intArray1[i+1]),int(intArray1[i+2])))
for i in range(0,len(intArray2),3):
	triangles.append(Triangle(int(intArray2[i]),int(intArray2[i+1]),int(intArray2[i+2])))

valid = 0
invalid = 0
for triangle in triangles:
	if(triangle.isValid()):
		valid+=1
	else:
		invalid+=1
print ("Valid: "+ str(valid))
print ("Invalid: "+ str(invalid))