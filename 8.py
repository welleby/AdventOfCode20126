#!/usr/bin/python
import re
import copy



input = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1"""

DEBUG = False
#DEBUG = True

class Screen:
	def __init__(self):
		self.w = 50
		self.h = 6
		self.screen = [["." for x in range(self.w)] for y in range(self.h)] 
	def rect(self, x,y):
		x = int(x)
		y = int(y)
		for yy in range(y):
			for xx in range(x):
				self.screen[yy][xx] = "#"

	def rotateCol(self, x,amount):
		original = copy.deepcopy(self.getCol(x))
		for y in range(self.h):
			self.screen[y][x] = original[(y-amount)%self.h]
	def rotateRow(self, y,amount):
		original = copy.deepcopy(self.getRow(y))
		for x in range(self.w):
			self.screen[y][x] = original[(x-amount)%self.w]
	def getCol(self,x):
		result = []
		for y in range(self.h):
			result.append(self.screen[y][x])
		return result
	def getRow(self,y):
		return self.screen[y]
	def getLitPixels(self):
		result = 0
		for y in range(self.h):
			for x in range(self.w):
				if self.screen[y][x] == "#": result+=1
		return result
	def __str__(self):
		result=""
		for y in range(self.h):
			row = ""
			for x in range(self.w):
				row+=self.screen[y][x]
			result+=row+"\n"
		return result

def debug(*input):
	if DEBUG: print(input)

def format(input):
	return input.split("\n")

def getInput():
	#return input
	file = open("8_input.txt","r")
	result = file.read()
	file.close()
	return result



def execInstruction(input, screen):
	x,y = re.findall(r"\d+",input)
	x = int(x)
	y = int(y)
	if input[0:4]=="rect":
		screen.rect(x,y)
	elif input[0:10]=="rotate col":
		screen.rotateCol(x,y)
	elif input[0:10]=="rotate row":
		screen.rotateRow(x,y)

screen = Screen()
inputArray = format(getInput())
for inp in inputArray:
	#print(screen)
	execInstruction(inp, screen)

print(screen)
print("Lit pixels: ", screen.getLitPixels())