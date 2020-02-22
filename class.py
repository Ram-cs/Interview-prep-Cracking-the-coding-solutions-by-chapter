'''
Naming
Type
Meaning
#######Public (name) ######
These attributes can be freely used inside or outside of a class definition.
#####Protected(_name) ######
Protected attributes should not be used outside of the class definition, unless inside of a subclass definition.
#######Private (__name) #########
This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.'''
#Data Encapsulation means, that we should only be able to access private attributes via getters and setters.

'''
PRIVATE===> attributes should only be used by the owner, i.e. inside of the class definition itself.
PROTECTED ==> (restricted) Attributes may be used, but at your own risk. Essentially, this means that they should only be used under certain conditions.
PUBLIC===> Attributes can and should be freely used
'''

class A:
    def __init__(self):
        self.public = "I am Public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def setter(self,protected, private):
        self._protected = protected
        self.__private = private

    def getter(self):
        print("I am : ", self._protected)
        print("I am : ", self.__private)

a = A()
# print(a.public)
# a._protected = "changed"
# print(a._protected)
#direct access to private can not be called

a.setter("PROTECTED", "PRIVATE")
a.getter()
#WRONG
'''There is still something wrong with our Robot class. The Zen of Python says: "There should be one-- and preferably only one --obvious way to do it." 
Our Robot class provides us with two ways to access or to 
change the "name" or the "build_year" attribute. This can be prevented by using private attributes, which we 
will explain later.'''

#here is correct way to declare the class
class A():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def SetX(self, x):
        self.__x = x

    def SetY(self, y):
        self.__y = y


#in the above class, can not access the private variables


############################
#### Class Attributes #########
########################

class A():
    a = "I am a class attributes"

x = A()
y = A()
print(x.a)
print(y.a)
x.a = "x is changing"
print(x.a)
print(y.a)
print(A.a)

A.a = "chaning the class attribute"

print(x.a)
print(y.a)
print(A.a)

print(x.__dict__)
print(A.__dict__)
print(y.__dict__)

#x not changed because Python's class attributes and object attributes are stored in separate dictionaries, as we can see here:

print(x.__class__.__dict__)




class Robot:
    def __init__(self,name=None,age=None):
        self.name = name
        self.age = age

    def setName(self,name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getInfo(self):
        print("My name is ", self.name, "age is ", self.age)


r = Robot()
r.name = "robert"
r.age = 20
    OR
r.setName("Robert")
r.setAge(20)

r.getInfo()

#WRONG
'''There is still something wrong with our Robot class. The Zen of Python says: "There should be one-- and preferably only one --obvious way to do it." 
Our Robot class provides us with two ways to access or to 
change the "name" or the "build_year" attribute. This can be prevented by using private attributes, which we 
will explain later.'''


# getter and setter
class P:
    def __init__(self,x):
        self.x = x

    @property
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    @x.getter
    def x(self):
        return self.__x
p = P(1001)
print(p.x)
'''Two things are noteworthy: We just put the code line "self.x = x" in the __init__ method and the property 
method x is used to check the limits of the values. The second interesting thing is that we wrote "two" methods 
with the same name and a different number of parameters "def x(self)" and "def x(self,x)". We have learned in a 
previous chapter of our course that this is not possible. It works here due to the decorating:'''

#a good way to do this without decorator
class P:
    def __init__(self,x):
        self.__set(x)

    def __set(self,x):
        if x < 0: self.__x = 0
        elif x > 1000: self.__x = 1000
        else: self.__x = x

    def __get(self):
        return self.__x

    x = property(__get ,__set) #make sure first put getter and then only setter, otherwise don't work


p = P(-1001)
p.x = 9999
print(p.x)

