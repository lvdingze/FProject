#类属性和实例属性
# 重要笔记：Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句。

class Person():
		pass
a = Person()

a.name = "lvdingze"
a.age = 18

print(a.name)
print(a.age)


'''
super() 函数用于调用下一个父类(超类)并返回该父类实例的方法。
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
'''

'''
class A:
     def __init__(self):
          print("enter A")
          print("leave A")
     # pass

class B(A):
     def __init__(self):
         print("enter B")
         A.__init__(self)
         # super(B,self).__init__()
         print("leave B")
     # pass
b = B()

'''
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')

		





