#coding=utf-8

#全局变量和局部变量
# 局部变量，就是在函数内部定义的变量
# 不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响
# 局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用


# 在函数外边定义的变量叫做全局变量
# 全局变量能够在所有的函数中进行访问
# 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
# 如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
a = 100

def function():
	a = 0
	print "a = " ,a

function()