#coding=utf-8

#字符串相关

#1.双引号或者单引号中的数据，就是字符串,python2不支持中文字符串遍历，但python3支持
name = "吕定泽"
name1 = '123456789'
#遍历输出每个字符,使用enumerate方法获取下标
for index,x in enumerate(name):
    print ("第%d个字符%s"%(index,x))

#2.下标和切片使用
print(name[0])
print(name[1])
print(name[2])

#切片的语法：[起始:结束:步长]
#d倒叙打印
print(name1[::-1])

#3.字符串常见操作
#3.1 find()
mystr = "my name is lvdingze, i like my name lvdignze" 
print("获取name的首字母index为%d"%(mystr.find("name")))

#3.2 index() 用法跟find一样，只不过如果查找str不存在 mystr中会报一个异常.(ValueError: substring not found)
print("获取name的首字母index为%d"%(mystr.index("lvdingze")))

#3.3 count(str) 返回 str在start和end之间 在 mystr里面出现的次数
print("name出现%d次"%(mystr.count("name")))

#3.4 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
print(mystr.replace("lvdingze","lyudingze",1))



