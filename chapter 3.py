###################################
######## Stacks and Queues ########
###################################

#1 Three in One:
three_in_one_stack = [[],[],[]]
three_in_one_stack[0].append(1)
three_in_one_stack[1].append(2)
three_in_one_stack[2].append(3)

for i in three_in_one_stack:
    print(i.pop())



#2 Stack Min:

class Stack:
    def  __init__(self):
        self.lst = []
        self.min = []

    def Push(self, val):
        self.lst.append(val)
        if len(self.lst) == 1:
            self.min.append(val)
        else:
            if self.min and self.min[-1] > val:
                self.min.append(val)

    def Pop(self):
        if self.lst:
            a = self.lst.pop()
        else: print(-1)
        if self.min and a == self.min[-1]: self.min.pop()


    def Min(self):
        if len(self.min) == 0: print(-1)
        else: print(self.min[-1])

s = Stack()
s.Push(1)
s.Push(2)
s.Push(130)
s.Push(-100)
s.Pop()
print(s.lst)
s.Min()


#3 Stack of Plates
class SetOfStacks:
    def __init__(self,limit):
        self.stack = []
        self.limit = limit

    def Push(self,val:int):
        if self.stack and len(self.stack[-1]) < self.limit:
            self.stack[-1].append(val)

        elif self.stack and len(self.stack[-1]) >= self.limit:
            self.stack.append([val])

        else: self.stack.append([val])

    def Pop(self):
        if self.stack:
            self.stack[-1].pop()
            if not self.stack[-1]:
                self.stack.remove([])

    def print_stack(self):
        print(self.stack)



s = SetOfStacks(2)
s.Push(1)
s.Push(2)
s.Push(3)
s.Push(4)
s.Push(5)
s.Pop()
s.Pop()
s.Pop()
s.Pop()
s.print_stack()


#5 Sort Stack

class sortStack:
    def __init__(self):
        self.stack = []
        self.stack.sort() #sorting
        self.stack.reverse() #smallest items are on the top

    #write other function like pop, push .......



#6 Animal Shelter

class AnimalShelter():
    def __init__(self):
        self.dog = []
        self.cat = []
        self.oneStack = []

    def enque(self,animal:int,type:str): #need to specific type so we know which animal it is, type is dog, or cat
        self.oneStack.append([type, animal])
        if type == "cat": self.cat.append(animal)
        else: self.dog.append(animal)

    def dequeueAny(self):
        if not self.oneStack: return -1
        t = self.oneStack[0]
        self.oneStack.remove(t)
        if t[0] == "cat":
            self.cat.remove(t[1])
        else: self.dog.remove(t[1])

    def dequeuDog(self):
        if not self.dog: return -1
        t = self.dog[0]
        self.dog.remove(t)
        self.oneStack.remove(["dog",t])

    def dequeuCat(self):
        if not self.cat: return -1
        t = self.cat[0]
        self.cat.remove(t)
        self.oneStack.remove(["cat",t])


animal = AnimalShelter()
animal.enque(1,"cat")
animal.enque(2,"dog")
animal.enque(3,"dog")
animal.enque(2,"dog")
animal.enque(5,"dog")
animal.enque(1,"cat")

print(animal.oneStack)
print(animal.dog)
print(animal.cat)

animal.dequeueAny()
animal.dequeuCat()
animal.dequeuDog()
animal.dequeuCat()


print(animal.oneStack)
print(animal.dog)
print(animal.cat)
