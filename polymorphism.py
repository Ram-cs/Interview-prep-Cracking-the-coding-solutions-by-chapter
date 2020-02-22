#################################
##### Polymorphism #############
###############################

#polymorphism (poly=many, morphism='form') ==> many form. Meaning that one function can be used in different places
#Abstract function ==> (this funciton must implement in the derived class) Functions which has only a singnature but it's functionality has not been defined yet # ==> can be used in polymorphism
#polymorphism can be achieved from overriding(overwriting) (using same signature and parameters) or overloading method (using same signature but changing the parameters)

import abc
class A(abc.ABC):
    @abc.abstractmethod
    def abstract(self, number): pass
        # raise NotImplementedError("Please implemtn this")
        #use to return the value

class B(A):
    def a(self, number,a):
        return number, a

    def abstract(self, number): #must redefine here, otherwise give an error
        return number


b = B()
print(b.a(1,2))


#SUPER in inheritance
class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(First):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

third = Third()


import abc
class Document(abc.ABC):
    def __init__(self,name):
        self.name = name

    @abc.abstractmethod
    def show(self): pass

class Pdf(Document):
    def __init__(self,name):
        super().__init__(name)

    def show(self): return (self.name + ": pdf content")

    def __str__(self): return self.show()

class Word(Document, Pdf):
    def __init__(self,name):
        super(Word, self).__init__(name)

    def show(self): return (self.name+": word content")


p = Pdf("Document1")
# w = Word("Document2")