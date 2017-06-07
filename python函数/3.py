#coding=utf-8

#range函数调用，表示一段范围
def printLine(count):
	for x in range(count):
		print "*"  * 10

printLine(10)



def add(a,b,c):
	return a+b+c

def avg(a,b,c):
	
	return add(a,b,c) / 3


result = avg(a = 1,b = 2,c= 3)

print result
