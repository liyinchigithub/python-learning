#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# test-class-object.py
# 封装类
# 其他python文件导入，类的实例化对象，进行引用类的方法和属性


'''
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    [方法]类中定义的函数。
    [类变量]类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    [数据成员]类变量或者实例变量用于处理类及其实例对象的相关的数据。
    [方法重写]如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    [局部变量]定义在方法中的变量，只作用于当前实例的类。
    [实例变量]在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
    [继承]即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    [实例化]创建一个类的实例，类的具体对象。
    [对象]通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
    类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
    区别于 Java 单继承
'''

from typing_extensions import Self


class test:
    # 构造函数（在类被实例化时候被调用）
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # 类中函数，第一个参数必须是self
    def sum(self):
        return self.a+self.b

result=test(1,2)# 实例化类的对象
print(result.sum())# 并引用其自定义方法，入参在实例化便传入，构造函数会在内部自定义

'''
    [类对象]
    类对象支持两种操作：属性引用和实例化。
    属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
    类对象创建后，类命名空间中所有的命名都是有效属性名。
    所以如果类定义是这样:
'''

class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
# 以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。

'''
    [构造函数]
    类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。
    __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
'''

class Complex:
    # 构造函数
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        # 其他类中函数可以通过selt.x引用构造函数中接收的变量，self代表类的实例，而非类
        # self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
        # [self 不是 python 关键字]，我们把他换成 runoob 也是可以正常执行的:
    def test(self):# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
        print("Complexl类test方法可以引用self.r:{}".format(self.r))
        print("Complexl类test方法可以引用self.i:{}".format(self.i))
        
# 类的实例化
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
x.test()


'''
[类的方法]
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
'''

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()



'''
    [继承]
    Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。
    [子类]（派生类 DerivedClassName）会继承[父类]（基类 BaseClassName）的属性和方法。
    BaseClassName（实例中的基类名）必须与派生类定义在一个作用域内。
    除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

'''
#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #[调用父类的构函]
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
 
s = student('ken',10,60,3)
s.speak()

'''
    [多继承]
    Python同样有限的支持多继承形式。
    注意:圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''

#类定义
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
 
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中参数位置排前父类的方法

'''
    [方法重写]
    如果父类方法的功能不能满足你的需求，可以在子类重写你父类的方法
    [super() 函数是用于调用父类(超类)的一个方法]
'''

class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法


'''
    [类属性与方法]
    类的私有属性
    __private_attrs：[两个下划线开头]，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

    类的方法
    在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
    self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定使用 self。

    [类的私有方法]
    __private_method：[两个下划线开头]，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。self.__private_methods。
'''

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量
 
    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量

# 类私有方法
class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
 
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
 
    def __foo(self):          # 私有方法
        print('这是私有方法')
 
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
x.__foo()      # 报错