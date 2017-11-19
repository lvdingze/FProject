#列表中的元素可以是不同类型的
test = ["aaa",111,"bbb",222]

#列表遍历
for x in test:
	print (x)

length = len(test)

i = 0
while i < length:
	print (test[i])
	i += 1

#列表增删改查
#添加元素("增"append, extend, insert)
test.append("ccc")
test.append("333")
print(test)

#修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改
test[3] = "hhh"
print(test)

#查找元素("查"in, not in, index, count)
#in（存在）,如果存在那么结果为true，否则为false
#not in（不存在），如果不存在那么结果为true，否则false

#待查找的列表
# nameList = ['a','b','c']
# findName = input('请输入要查找的姓名:')
# if findName in nameList:
#      print('在字典中找到了相同的名字')
# else:
#      print('没有找到')


#删除元素("删"del, pop, remove)
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除
del test[1]
print(test)
test.pop()
print(test)
test.remove('hhh')
print(test)

#排序(sort, reverse),sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。
test.sort()
print(test)
test.reverse()
print(test)



