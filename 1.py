#!/usr/bin/python
#http://adventofcode.com/2016/day/1
input = """R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, 
R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, 
R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, 
R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, 
L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, 
L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, 
L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, 
L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3"""

#input = "R8, R4, R4, R8"
from copy import deepcopy
import re

class Pos:
	def __init__(self):
		self.dir = 0
		self.x = 0
		self.y = 0
	def __str__(self):
		return "X:%i; Y:%i" % (self.x, self.y)
	def __eq__(self,other):
		return self.x == other.x and self.y == other.y
	def updateDir(self,input):
		if(input[0]=='R'):
			self.dir=(self.dir+1)%4
		elif(input[0]=='L'):
			self.dir=(self.dir-1)%4
	def walk(self, input, step):
		self.updateDir(input)
		steps = []
		if(self.dir==0):
			for i in range(int(input[1:])):
				self.y+=1
				steps.append(deepcopy(self))
		if(self.dir==1):
			for i in range(int(input[1:])):
				self.x+=1
				steps.append(deepcopy(self))
		if(self.dir==2):
			for i in range(int(input[1:])):
				self.y-=1
				steps.append(deepcopy(self))
		if(self.dir==3):
			for i in range(int(input[1:])):
				self.x-=1
				steps.append(deepcopy(self))
		print("Step: %i; Input: %s; Pos: %s" %(step, input, self))
		return steps

def calculatePosition(inputArray):
	answer = Pos()
	positions = []
	step = 0
	for way in inputArray:
		positions.extend(answer.walk(way,step))
		step+=1
	return answer, positions

def findFirstDupe(inputArray):
	first = len(inputArray)
	for i in range(len(inputArray)):
		for j in range(i+1,len(inputArray)):
			if(inputArray[i] == inputArray[j]):
				print("First dupe: %i and %i; Position: %s" % (i,j,inputArray[i]))
				return inputArray[i]
	print("No dupes")



input = re.sub("[\r\n ]", "", input)
inputArray = input.split(",")
answer, positions = calculatePosition(inputArray)
print(answer)
print("Length: %i" % (abs(answer.x) + abs(answer.y)))

dupe = findFirstDupe(positions)
print("Length: %i" % (abs(dupe.x) + abs(dupe.y)))
#pos = calculatePosition()
#print(pos)