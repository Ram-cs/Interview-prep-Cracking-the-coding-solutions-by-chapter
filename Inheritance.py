#
class Vehicle:
    def __init__(self,brake=0, accelerate=0):
        self.brake = brake
        self.accelerate = accelerate

    def accelerate(self, accelerate):
        self.accelerate = accelerate

    def brake(self, brake):
        self.brake = brake


class Car(Vehicle):
    def __init__(self, brake, accelerate):
        Vehicle.accelerate(accelerate)
        Vehicle.brake(brake)



class Person:
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.__private = 0 #private member can not access from outside even with the instance of Person Object

    def assignName(self,first,last):
        self.firstName = first
        self.lastName = last


    def getName(self):
        return self.firstName + " " + self.lastName


class Employee(Person):
    def __init__(self,first, last, number):
        self.employee = number
        Person.__init__(self)
        Person.assignName(self,first,last)


    def getName(self):
        print(Person.getName(self))
        print(self.employee)


class C:
    def __init__(self):
        Person.__init__(self)
        self.ok = 5

e = Employee("Ram","Yadav", 1001)
e.getName()
e.firstName = "Changed"
e.lastName = "Changes"
e.getName()
print(e.firstName)
print(e.lastName)
print(e.employee)
Person.getName()

c = C()
print(c.firstName)