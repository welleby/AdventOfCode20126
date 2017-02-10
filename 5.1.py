#!/usr/bin/python
import hashlib

input = "ffykfhsq"
#c6697b55

def getPassword(input):
	result = ""
	for i in range(0,999999999):
		m = hashlib.md5()
		m.update(("%s%i"%(input,i)).encode('utf-8'))
		if(m.hexdigest()[:5]=="00000"):
			result+=m.hexdigest()[5]
			print(m.hexdigest())
		if(len(result)==8):
			break
	return result

print(getPassword(input))
	#if(m.hexdigest()[:
#m.update('abc3231929'.encode('utf-8'))
#m.update('b'.encode('utf-8'))
#m.update('c'.encode('utf-8'))
#print (m.hexdigest())