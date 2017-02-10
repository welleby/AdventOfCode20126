#!/usr/bin/python
import hashlib

#input = "abc"
input = "ffykfhsq"
#c6697b55

def isValidInt(input):
	try:
		i = int(input)
		if i<8:
			return True
	except ValueError:
		return False
	return False

def getPassword(input):
	result = {}
	for i in range(999999999):
		m = hashlib.md5()
		m.update(("%s%i"%(input,i)).encode('utf-8'))
		if(m.hexdigest()[:5]=="00000"):
			print(m.hexdigest())
			if isValidInt(m.hexdigest()[5]):
				#print(m.hexdigest()[5])
				if m.hexdigest()[5] not in result:
					print("Adding %s to %s"%(m.hexdigest()[6],m.hexdigest()[5]))
					result[m.hexdigest()[5]]=m.hexdigest()[6]
					#print(m.hexdigest())
		if(len(result)==8):
			break
	return result

dict = getPassword(input)
result = ""
for com in sorted(dict):
	result+=dict[com]

print(result)

#print(isInt("6"))
	#if(m.hexdigest()[:
#m.update('abc3231929'.encode('utf-8'))
#m.update('b'.encode('utf-8'))
#m.update('c'.encode('utf-8'))
#print (m.hexdigest())