#coding:UTF-8
print("小刀测试程序")
while  (0):
	knift = input("please input knift length:")
	if knift <= 10 :
		print("go to ")
	else :
		print("do not go ")


namelist = ["lvdingze","abd", "aaa" ,"lvdingze"]

for temp in namelist :

	while  temp == "lvdingze":
			print(temp)
			break;

namelist.append("haha")

namelist.remove("aaa")
print(namelist)

str = "adcde,nnn"
str = str.split(",")
print(str)


