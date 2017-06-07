#coding=utf-8

#四种函数类型
#有参、无参
#有返回值。无返回值

#默认参数一定要位于参数列表最后面
def printInfo(name,age = 35):
	print "Name: ",name
	print "Age: ",age

printInfo(name = "lvdignze")
printInfo(age = 90,name = "haha")

#不定长参数函数

def fun(a,b,*args,**kwargs):
	"可变参数演示实例"
	print "a = ",a
	print "b = ",b
	print "args = ",args
	print "kwargs = "
	for key,value in kwargs.items():
		print key, " = ",value

fun(1,2,3,4,5,m=6,n=7,p=8)
