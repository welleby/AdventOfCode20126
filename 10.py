#!/usr/bin/python
from helper import *
from copy import deepcopy
import re


input = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""

input = getInput("10_input.txt")
class Robot:
	def __init__(self, name):
		self.value = None
		self.high = None
		self.low = None
		self.name = name
	def __str__(self):
		return "Name: %s; High: %s; Low: %s" %(self.name,self.getHigh(), self.getLow())
	def takeInstruction(self,instruction):
		self.instructions.append(instruction)
	def canExecute(self):
		return self.value is None and self.high is not None and self.low is not None
	def executeInstruction(self,instruction):
		self.give(instruction["lowBot"],instruction["highBot"])
	def getHigh(self):
		return deepcopy(self.high)
	def getLow(self):
		return deepcopy(self.low)
	def getValue(self):
		return deepcopy(self.value)
	def has(self,value1, value2):
		return (self.high == value1 or self.low == value1) and (self.high == value2 or self.low == value2)
	def give(self,lowBot,highBot):
		if self.has(61,17):
			print("FOUND: ",self)
		lowBot.take(self.getLow())
		highBot.take(self.getHigh())
		self.high = None
		self.low = None
	def take(self,value):
		value = int(value)
		if self.value is None:
			self.value = value
		else:
			self.high = max(value,self.value)
			self.low = min(value,self.value)
			self.value = None
def runBots(instructions):
	bots = dict()
	while instructions:
		instruction = instructions.pop(0)
		#print (instruction)
		if instruction[:5] != "value":
			fromBot, low, high = re.search("(bot \d+) gives low to (.*? \d+) and high to (.*? \d+)",instruction).groups()
			fromBot = createAndGetBot(bots,fromBot)
			if not fromBot.canExecute():
				instructions.append(instruction)
			else:
				low = createAndGetBot(bots,low)
				high = createAndGetBot(bots,high)
				fromBot.executeInstruction({"lowBot":low,"highBot":high})
				#fromBot.execute()
		else:
			val, name = re.search("value (\d+).*(bot \d+)",instruction).groups()
			bot = createAndGetBot(bots,name)
			bot.take(val)

	return bots
def printBots(bots):
	for k, v in bots.items(): print (v)
def createAndGetBot(bots,name):
	if name in bots:
		return bots[name]
	else:
		bots[name] = Robot(name)
		return bots[name]
input = format(input)
bots = runBots(input)
print(bots["output 0"].value * bots["output 1"].value * bots["output 2"].value) 