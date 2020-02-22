##########################################################
######### THIS IS ONLY A RANDOM TESTING ##################
##########################################################

for i in range(5):
    for j in range(5, 10):
        if(j == 7):
            print(j)
            break
    else:
        print("executin")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
 #loop fell through without finding a factor
        print(n, 'is a prime number')

def sum(a, b):
    return a + b

print(sum(2,3))

sum_dup = sum(4,4)

print(sum_dup)

#FUNCTIONS
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')

def check():
    if '3' in ('4', '5', '6' ,' 7', '8' , '3'):
        return True;
    else:
        print("executed")
        False
print(check())

i = 5

def f(arg=i):
    print(arg)

# i = 77
f()

def f(a, L=[]):
    L.append(a)
    return L


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

a = f(1)
print(f(1))
print(f(2))
print(f(3))
print(f(55))


print(a)

a = [1,2,3]
b = a

print(b)
print(id(a))
print(id(b))

def check():
    a = [1, 2, 3]
    b = a
    c = []
    d = []

    print(id(c))
    print(id(d))

    if c is d:
        print("pointing to same object")

    if c == d:
        print("same")

check()

a = '54.0'
print(type(a))

def make_incrementor(n):
    return lambda x: x + n

a = make_incrementor(33)
print(a(3))
print(a(4))

#LIST
a = list(range(1,5))
a = a + list(range(-3,19))
a.reverse()
print(a)

#QUEUE
from collections import deque
a = deque()
a.append([(1,2)])
def a(a:deque()):
    print(a.popleft())
a(a)


queue = deque([(1,2),(15,3)])
print(queue)
queue.append((5,4,5,29))
print(queue)
a,b = queue.popleft()
print(a)
print(b)
print(queue)

squares = list(x**2 for x in range(10))
squares = list(map(lambda x: x**2, range(5)))
print(squares)

a = list(j for i in [1,2,3] for j in [1,2,3] if i== j)
b = [j** 2 for j in a]
print(a)
print(b)

vec = [[1,2,3], [4,5,6], [7,8,9]]
vec = [(element, element) for i in vec for element in i]
print(vec)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit = [[i.strip()] for i in freshfruit] #strip helps to remove the space (rstrip(), lstrip())
print(freshfruit)
del(freshfruit[:])
print(freshfruit)

#SETS (https://realpython.com/python-sets/)
#TUPLES: is hsable to sets but list is unhashable
#update(iterable) ==> TO ADD MULTIPLE ITEMS AT ONCE USE
#add(one item) ==> TO ADD ONE ITEMS
#remove(one item)==> TO remove 1 item
#difference_update(iterable)==>To remove multiple item
#difference()==> use to give the difference of two sets
#symmetric_difference() ==> give the elements that are either in set1 and set2 but not in both
#disjoint(set2) ==> return boolean, giving whether two sets have any elements common or not:: True means the set is disjoint and has not element common
#issubset(set2)==> return boolean if one set is subset of other, subset of set means every elements in s1 is also on s2 as well
# a = set('123456')
# b = set('120923')
# print(a^b)

a = [1,2,3]
b = [1,2,4,5]
a = set()
a.update([1,2,3,4,5,6,1])
a.update([1,2,3,4])
a.update((1,2,3,4))
b = a.copy() #to copy the set otherwise will point to the previous object
b.remove(1)
b.difference_update([3,444])
print(a)
print(b)
print(b-a)

c = set()
c.add("abc")
print(c)
a = set(a)
b = set(b)

a.update(b)
a |= b #same as above line

print(a.intersection(b)) #doesnt update set a
a.intersection_update(b) #update set a with intersection of a and b
a &= b #same as above line
a.difference_update(b) #update set a by a-b result
a -= b #same as above line
a.difference(b) #it just print the different but doen't update set a
print(a.symmetric_difference(b)) #print out the result of elements that are not in a and b, but doesn't update any sets
a.symmetric_difference_update(b) #update the set a with the symmetric difference
a ^= b same as above line

a.difference_update([1,2])

#NOTE:-===> using operator like a &= b, both a and b must be set, but using a.intersection_update(b), here b may be set or any iterable list, tuples or dictionary
print(a.isdisjoint(b))
print(a)



#TUPLES
# a = '2323', 2323, '4'
# print(a)


#DICTIONARY
import collections
a = [1,2,2,1,1,3,4,5,2,1]
dic = collections.Counter(a)
#
# #NOTE: dictionary perform intersection(d1&d2) and (d1-d2) but but union (d1.update(d2))
import collections
#Tubles is Hashable to dic but list is unhshable
c1 = collections.Counter([1,1,2,2])
c2 = collections.Counter([1,1,1,1,2,2,2,9])
print(c1&c2) #intersection
print(c1-c2) #difference
print(c1)
print(c2)
c1.update(c2) #union
print(collections.Counter(list(c1.elements())+list(c2.elements()))) #union but long way
print(dic.most_common())
print(dic.pop(1)) #pop the specific element
dic.update([1,1,1])
dic.update([21]) #update==> if item already exists increase it's number otherwise add new to dictionary
dic.update([21])
dic[1] = 3 #change the value of
print(list(dic.elements())) #gives all the different values in the form of list
dic.pop(1) #take out the specified value
a = dic #this is shallow copy, which means  a points to dic, changing a will change dic
a = dic.copy() #this is deep copy, changing a doesn't change original dic
print(a)
a[1] = 55
print(a)
c = {}
c = c.fromkeys((1,2,3,10),22) #from key helps to create a new dictionary with the key specified
print(c)
dic.clear() #clear all the dictionary
print(dic.get(11)) #difference between this and dic[11]==> this method return None if the elements is not in directory, but other method returns 0
print(dic[11])
print(dic)



dic = {}
dic[1] = 0;
dic[2] = 9;

a = {x:x**2 for x in (1,2,4)}
lis = list(a)
print(a)
print(lis)
print(lis.count(1))

for x, y in a.items():
    print(x)
    print(y)

for x, y in enumerate (['banana', 'apple', 'orange']):
    print(x,y)




#LOOP TECHNIQUES
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

print(list(zip(questions, answers)))
for x, y in zip(questions, answers):
    print(x, y)


for i in reversed(range(2,10)):
    print(i)

for x in sorted(questions):
    print(x)



basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
b = set(basket)
print(b)
print(sorted(set(basket)))
a = [i for i in sorted(set(basket))]
print(a)

n = set(basket)
print(n)

a = list(range(1, 10))
b = a[:]
print(id(a))
print(id(b))
b.pop(0)

print(a)
print(b)
b = ['1','2','3','4','5'] #value must be a string
d = {'a': 1, 'b': 5}
a = '    '
print(a.join(d))

s = "my home town is is Nepal"
print(s.split("town"))
b = s.split("town")
print('___'.join(b))
print(s)


l = [1,2,3]
m = [1,1,78,8,9]
l.extend(m)
print(l)
spam =42
print(id(spam))

#IMMUTABLE MEANS: two variable DOESN'T POINT to the SAME OBJECT, after changing one variable doen't change another variable
#MUTABLE: if two variable point to the SAME OBJECT, after changing one variable other will reflect change
a = "ram"
b = a
b += "sita"

print(a)
print(b)

print(id(a))
print(id(b))

a = (1,2,3,4)
b = a
b += (33,22,22)
print(a)
print(b)
print(id(a))
print(id(b))

#SETS are MUTABLE
#TUPLES are IMMUTABLE
#NOTE: pop() remove random elements from the set, USE remove() instead
a = set([2,3,4,5])

b = a
b.add(78)
b.remove(5)
print(a)
print(b)

print(id(a))
print(id(b))

A ={'a', 'b', 'c', 'd'}
A.remove('a')
print(A)

l = [3,9,1,99,0]
l.sort()
#OR
l = sorted(l)
del(l[0])
print(l)


a = {1:'a', 2:'b', 3:'c'}
a[4] = 'D'
print(a)

l = [2,2,1,3,4, 1, 1,5]
l2 = [21,21,11,31,41, 11, 11,51]
l = [i for i in l[:] if i != 1]
print(l)
for i in l[:]:
    if i is 1:
        l.remove(i)
j = 0
for i in l[:]:
    if i is not 1:
        l[j] = i
        j += 1
print(l)
#
#http://book.pythontips.com/en/latest/map_filter.html (map, reduce, filter)
# #MAP (function to apply, iterable) #returns the value at the end, can have more than one iterable
# #LAMBDA (parameter: expression)
# #FILTER(function, iterable), can only have one eterable
#zip ==> map the similar index of multiple container, to unzip zip(*mapped) https://www.geeksforgeeks.org/zip-in-python/

print(list(map(lambda x: x != 1, l)))
l = list(filter(lambda x: x != 1, l))
print(l)
#
a = map(lambda x: x, "abcd")
print(list(a))

print(list("abc")) #must put iteratble object
print(list("12345"))
print(list("abc"))
s = ["abc", "abd", 'abm']
print(list(zip(*s)))
print(list(map(list, s)))
a = (map(list, s))
print(list(a))
a=map(list,zip(*s))
# print(list(a))
# # print(a)
res=""

for i in list(a):
    print(i)
    if [i[0]]*len(i)==i:
        print("=====>", res)
        res=res+i[0]
    else:
        break

b = ["", ""]



print(("poilt").split('o'))
print(['a']*4)


# add = lambda x: x*2
#
# print(list(map(lambda x: x*2, [1,2,3,4])))

dict_a = [{'name': 'python', 'point': 9}, {'name': 'java', 'point': 8}]
print(list(map(lambda x: x['name'] == 'python', dict_a)))
print(list(filter(lambda x: x['name'] == 'python', dict_a)))
#
list1 = [1,2,5,10]
list2 = [10,20,30, 90]
print(list(map(lambda x, y: x+y, list1, list2)))
print([i for i in list1 if i in list2])
#REDUCE :
'''Reduce Working :

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console '''

from functools import reduce

print(reduce(lambda x,y: x + y, list1,5)) #HERE, x =5 and y is the each elements from list1

S = "abbaca"
# print(reduce(lambda s, c: s if s == c else s + c, S, "#")) #<==> is same with print(reduce(lambda s, c: s + c, S, "#"))
class Human:
    def __init__(self, givenAge):
        self.gender = None
        self.age = givenAge

    def m_gender(self, mygender):
        if type(mygender) is str:
           self.gender = mygender
        else:
            print("must be string")
            return

    def clear_gender(self):
        self.gender = None

    def get_gender(self):
        return self.gender

class Person(Human):
    def __init__(self, firstName, lastName, age):
        Human.__init__(self, age)
        self.first = firstName
        self.last = lastName

    def fullName(self):
        print(self.first + self.last)


p = Person("Ram", "Yadav", 20)
p.m_gender("Male")
print(p.get_gender())
p.fullName()
print(p.age)

a = [1,2,3,4,5]
a.pop()
a.pop()
a.append(8)
print(a)


import queue
q = queue.Queue()



print(q.qsize())


#STACKS

class Stack:
    def __init__(self):
        self.list = []

    def insert(self, x):
        self.list.append(x)

    def size(self):
        print("size ==>", len(self.list))

    def print(self):
        for i in self.list:
            print(i)

    def delete(self):
        self.list.pop()

s = Stack()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(6)
s.size()
s.print()
s.delete()
s.size()
s.print()

#QUEUE==> it is almost similar to the list, but it has extra function like popleft()....
import queue
a = queue.deque()
a.append(1)#can only put a signle items
a.append(4)
a.extend([1,2,3]) #extend helps to put multiple items in the queue
print(a)
a.pop() #pop the last element of the queue
a.popleft() #pop the first element of the queue
a.reverse() #reverse the queue
a.appendleft(999) #append to the beginning of the queue
a.append(898) #appaned to the last of the queue
a.extendleft([111,111]) #must be iterable items, can be use to add multiple items to the beginning of the queue
print(a)
a.rotate() #bring the last element to the front of the queue
# a.remove(111) #remove the elements, if elements is not in the queue, give an error
# print(a.count(111))
# print(a.index(111,2))

print(a)

q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put("werert")


print(q.empty())

while(not q.empty()):
    print(q.get())

print(q.empty())


l = [1,2,3,4,5, "string"]
print("length==>",len(l))
for i in l:
    l.pop(0)
    print(i)


print("length==>",len(l))

a = [1,2,3,4]
c = a #SHALLOW COPY
b = a[:] #DEEP COPY

b.pop()
b.pop()

print(a)
print(b)



class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class BinaryTree:
    def __init__(self):
        self.node = None

    def insert(self, x):
        if self.node is None:
            self.node = Node(x)
            return
        else:
            temp = self.node
            while True:
                if x == temp.val:
                    return
                elif x < temp.val:
                    if temp.left is None:
                        temp.left = Node(x)
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(x)
                    else:
                        temp = temp.right

    def display(self):
        q = queue.Queue()
        temp = self.node
        q.put(temp)

        while not q.empty():
            a = q.get()
            print(a.val)

            if a.left is not None:
                q.put(a.left)
            if a.right is not None:
                q.put(a.right)








b = BinaryTree()
b.insert(10)
b.insert(4)
b.insert(12)
b.insert(14)
b.display()


result = [int]



print(result)
print(type(3))


a = [1,3,6,7,8,3,5,0]


print(a[::-1])

a = "abc"
print(a[::-1])
b = ["abc", "abd", "avm"]



count = 0
# for i in range(4):
#     count += 1
#
# print(count)

while(True):
    if count == 2:
        break
    for i in range(len(a)):
        a[i] += 1
    count += 1

print(count)
print(a)

s = "abcdef"
print(s[70:])


a:int = 5
b:chr = 'a'
print(type(a))
print(type(b))

nums1 = [1, 2]
nums2 = [3, 4]

a = nums2 + nums1

a.sort()
print(int(3/2))

a = [i for i in str(120)]
a.reverse()
print(a)
a = ''.join(a)
print(a)

a = "my guest is the home"


print(a)
print(int(a[::-1]))
print(-2**32)




print(s.find('b'))

a = ["acv","a", "v", "ddfdcdsd"]
print(max(a, default=0))

for i in range(len(s)):
    print(s[i])


for i in range(0,5):
    print("outside==>", i)
    for j in range(i,5):
        print("inside ==> ",j)
for i in range(0,len(a)):
    print(a[i])

for index, value in enumerate(a):
    print(index, value)

print(max(a))

a = [2,2,2,2]
print(len(a))
print(a.count(2))
print(a.index(2))

for index, value in enumerate(a):
    print(index, value)

a = [1, 2, 3, 4, 5]

print(str(a)[1:])
print(a.count(2))
if (2 in a) is True:
    print("Inside")



a = "abc+efg.mnog@gmail.com"
print(a[:a.index('+')])
print(a[a.index("@")+1:])

a = a[:a.index("+")] + a[a.index("@"):]

print(a)

print(a.replace("--", ""))

a = []

print(a[-1])

print(a.replace(".","", 1))

a = set()
a.add(2)
a.add(3)
a.pop() #remove an arbitrary element from set

print(len(a))

a = 7
b = 9

a,b = b,a
print(a, b)


a = {1,1,1,2,2,2,33,4,4,5}
print(list(a))

a = [1,2,3]
print(a[-2])

k = 0
while (k < 0):
    print("In")

#COUNTER
import collections

# counter = collections.Counter(['a', 'b', 'c','d'])
# print(counter)
n1 = [1,2,3,4,1,2,6,7]
n2 = [1,3,5,3,1,2,6,0]

index = -1


while index >= -(len(n1)) :
    print(n1[index])
    index -= 1

print(int(10014/10))


for i, j in enumerate(n1):
    print(i, j)

print(set(n1) & set(n2))


print(set([1,2,3,4,4]))



b = [j** 2 for j in a]
b = [i * 2 for i in n1]



s = "Hello 12345 World"
s = s.split(' ')
print(s)

print('  000  '.join(s)) #JOIN INDIVIDUAL ELEMENT OF THE LIST

[i for i in s if i =='a' or i =='e' or i == 'i' or i == 'o' or i == 'u']

[i for i in s if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u']


a = list(s)
a = ''.join(a)

print(a)

a = set('AEIOUaeiou')


if ('i' in a) == True:
    print("INSIDE")



a = set('122334')
print(a)

A = [2,7,4]
''.join([str(x) for x in A])
a = ''.join([str(x) for x in A])
a = int(a)
print(a+10)

a = 12345

b = map(int, str(a))
print(list(b))

a = '1223'
b = '124'

from itertools import zip_longest
print(list(zip_longest(a,b,fillvalue=0)))

print(divmod(123,10))

a = "0"*2 + a
print(a)

c = map(lambda x, y: int(x) + int(y), a, b)
c = list(c)
print(c)
print(''.join(str(i) for i in c))

import math


print(int(math.sqrt(8)))
print(math.log2(832))

print(4 // 3)
print(int(4 ** 0.5))

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(nums1[:3])

for i, j, k in zip(range(5), range(5)):
    print(i, j)
A=[4,2,5,7]
for i, k in enumerate(A[:]):
    if k % 2 == 0 and i % 2 == 0:
        print("Fist", i, k)

if 2 % 2 == 0 and 1 % 2 == 0:
    print("IN")

a = 4
b = 6

a,b = b,a



a = b = 88
a = 999
print(id(a), id(b))

print(a)
print(b)
#STAR (*) ==> MEANS UNPACK THE VALUE, * USESES FOR TYPLES OR LIST OR OTHER BUT ** USES FOR DICTIONARY https://stackoverflow.com/questions/11315010/what-do-and-before-a-variable-name-mean-in-a-function-signature

a = ["bella","label","roller"]

import collections
d = collections.Counter(a[0])
print(list((d & collections.Counter(a[1])).elements()))

b = [set(x) for x in a]
print(b)
print(b[0])
print(b[1:])
print(b[0] & (b[2])) #intersection but unhasable
print(list(b[0].intersection(*b[1:]))) # first unpack and then iterate over all sets elements

b = [collections.Counter(x) for x in a]

a = b[0]

for i in b:
    a = a & i
print(list(a.elements()))


l = ['abc', 'adb', '9283a74bg', 'boys and girls']
sets = [set(x) for x in l]
print(sets)
print(sets[0].intersection(*sets[1:]))


a = [[1,2,3], [2,1,4], [4,3,6]]

for i, y in a:
    print(i,y )

b = [1,2,3,4]

print(sum([i for i in b]))

print(list(sum(i) for i in a))

print(sum([i for i in a if i % 2 ==0]))

b = list(map(sum, a))
print(b)


print(list(map(lambda x: [i for i in x if i% 2 == 0],a)))

print(list(map(sum, a)))

import time

for i in a:
    print(i)
    time.sleep(1)

queries = [[1,0],[-3,1],[-4,0],[2,3]]

for x, k in queries:
    print(x, k)

if 2 < 4: print("4 is greater")

result = []

for i in range(4):
    result.append([])

print([[] for i in range(4)])
print(result)

result[0].append((1))
print(result[0])

print([ [*i] for i in zip(*[[1,2,3],[4,5,6],[7,8,9]])])

print(zip(*[[1,2,3],[4,5,6],[7,8,9]]))

print([1,2] == [1,23])

a = [1,52,3,4,6]
reversed(a)
print(a)

a = [1,2,3,2,3,4,4,5,6,4]
b = [3,2]

print(set(a) ^ set(b))
print(set(range(1,7)))

print(sum(i for i in a))
import statistics
print(statistics.mode(a))


b = collections.Counter(a)
print(b)
print(list(b.elements()))

for x in reversed(a):
    print(x)

a = 2
b = 6

b, a = a, b #don't need temp varaible like below
temp = a
a = b
b = temp

print(a, b)

a = [1,2,3,4,5,6]
print(a[::2]) #every 2nd elements of list

print(type(bin(5)))
print(a.count(1))


print("-.-." + "-..." + ".-")

b = []
print(b[-1])

b = ["abc", "def", "ghi"]
print(b[::-1][::-1])

b = set()
b.add(2)
print(b)

print("".join(sorted("ancid")))

print([i if i ==2 else 4 for i in a])


for i, j in enumerate(a, 1):
    print(i, j)

print("!".isalpha())

b = "   "

b = b.strip()
if b:
    print("Yes")
else:
    print("Not true")
print(b)
# b = b.replace(b[0], "999")
# print(b)

# b = [None]*10
# b[9] = 12
# print(b)



print(bool(""))

b = "7_28]"
print(list(b))

b = collections.Counter(a)

for item in b:
    print(b[item])

s = "abcdefg"

r = [s[i:i+2] for i in range(0,len(s), 2)]
print(r)

for i in range(0,100,39):
    print(i)

[i for i in range(4) if i < 2]
b = "Bob hit a ball,   the hit's   BALL flew far after it was hit."
b = b.strip()
print(b)
The strip() removes characters from both left and right based on the argument (a string specifying the set of characters to be removed). If the chars argument is not provided, all leading and trailing whitespaces are removed from the string.
c = collections.Counter(["a", "a", "b", "c","c","c"])
# c.pop("d", None) #remove the specific key, otherwise remove none
c = c.most_common()[0][0] #arrange in dessending order the key of the dictionary and getting the firt most occured element
print(c)

b = b.replace('^A-Z0-9', '')
print(b)
print(b.split(" "))

import string
print(string.punctuation)

for p in string.punctuation:
    b = b.replace(p, "")
print(b)

print("".join(b.split(' ')))

b = "a, a, a, a, b,b,b,c, c"
# print(b.split(" "))

import re
re.findall()


if 2 is not 0:
    print("a")

print("abc"*3)

if len(a) != 4:
    print("Yes")

NOTE: FIND AND INDEX WORKS SAME WAY, BUT FIND RETURN -1 IF SUSTRING NOT FOUND WHILE INDEX GIVE ERROR
print(("Let it be, let it be, let it be").find("let it"))
print(("Let it be, let it be, let it be").index("let it"))


chars = "abcsd"
c = collections.Counter(["a","a","b","b","c","c","c"])
print(len(c.values()))

RECURSIVE FUNCTIONS
def factorial(n):
     if n == 0 or n == 1: return 1
     return n * factorial(n-1)

# print(factorial(5))
from typing import List

# List[int]

a = [1,3,8,5]

def addList(l: List[int]):
    if len(l) == 0: return 0
    return l[0] + addList(l[1:])

print(addList(a))

def printReverseList(l:List[int]):
    if len(l) == 0: return
    printReverseList(l[1:])
    print(l[0])

printReverseList(a)

a = [1,1,2,8,2,1,3,5]
def ListLargestValue(l:List[int]):
    if len(l) == 1:
        return l[0]
    # return max(l[0], ListLargestValue(l[1:]))

    m = l[0]
    print("M ==>", m)
    a = ListLargestValue(l[1:])
    print("A  ==>", a)
    print("M before ==>", m)
    if m < a:
        m = a
        print("IN ==>", m)
    print("After", m)
    return m # m NEVER ASSIGNED to the TOP m = l[0] instead m = ListLargestValue(l[1:])

ListLargestValue(a)

def numCountInList(l:List[int], num:int):
    if len(l) == 0: return 0

    a = numCountInList(l[1:], num)
    if num == l[0]:
        a += 1

    return a


print(numCountInList(a, 1))
#
# if 8 < 8:
#     print("IN")

if 8 <= 9 <= 90:
    print("true")

# print(float('inf'))
a = None
# if a:
#     print("IN")
#

a = [1,2,3,4,5]
b = [1,2,44]

print(set(a) & set(b))

def isValPresent(l: List[int], val:int):
    if not len(l): return
    isValPresent(l[1:], val)
    return val in l

print(isValPresent(a, 11))

def giveRestList(l:List[int], val:int):
    if not len(l): return -1
    if l[0] == val: return True
    return giveRestList(l[1:], val)

print(giveRestList(a,2))

def addUpToVal(val:int):
    if val == 0: return 0
    return val + addUpToVal(val-1)

print(addUpToVal(888))
nums = []
target = 9

# [i if nums[i] == target else -1 for i in range(len(nums)) ]

# print(type(1) == float)

a = "aabc"
print(a.split(" "))
c = "acdsc"
a = collections.Counter(a.split(" "))
print("a" in a)
print(a[:] == a[::-1])

print(all(char in c for char in a))
print(([char for char in a]))

print(set(["acv", "scd"]))

print(collections.Counter("abca") + collections.Counter("aaaa"))
a = collections.Counter("abca") + collections.Counter("aaaa")
print(list(zip(a.keys(), a.values())))

#ITERATING IN DICTIONARY
for w, i in list(zip(a.keys(), a.values())):
    print(w,i)

print(type([]) == list)

#REGEX TO EXTRACT THE ALPHABETS OR STRING FROM THE STRING
import re

a = "a123b98c2323"
print(''.join(re.findall("[0-9]",a)))



a = "abc"
b = "aabmn"
a = collections.Counter(a)
b = collections.Counter(b)
print(a.keys())
print(a,b)
print(a & b)

#MINIMUM
print(min("abc", "a", key=len))

print(list(filter(lambda x: x.isalpha(), "ab124")))



import math
math.sqrt()

a = [True, False, False]

print(a[0:1:2])



a = [1]*3
a[0:] = [2,4,5]

[a[i] = i for i in range(4)]

a = [1,2,3,1]
# print(a.count(1))

dic = {}
dic[1] = 9
dic[1] = 00

p = "acbcdefgsadfasdfasdfasdfsafd"
for i in range(len(p)):
    print(p[i:i+2])

print([1,2] in [1,2])

p = sorted(p)
print(p == ['a','b'])

if 2 > 2:
    print("greater")

a = set("abc")
b = set("cab")

print(a == b)


a = collections.Counter("abc")
b = collections.Counter("cbac")

print(a == b)

l = [1] * 2
# # l[0] = 1
# print(l)
PERMUTATION
import itertools
print([''.join(perm) for perm in itertools.permutations("abc")])

ALL (all(iterable), return True if all items in iterable are true otherwise returns false)

MAX number
print(float('inf'))
#MIN number
print(float('-inf'))

from collections import deque

a = deque([(1,0)])
a.append((4,3))
a.extend([1,2,3,44])
# a.popleft()
print(len(a))
print(a)

a = "       abc dsde dsf          sdf          "
print(a.replace(" ", ""))

a = (1,3)
a + (4)
print(a)

a = [13,4,5]
a.remove(4)
print(a)

d = {1:2,5:6}

for x, v in d.items():
    print(v)


print(3 in d)

print(sum([1,2,3]))


a = [[1,2],[1,3],[2,3]]
b = set()
s = [(i[0] for i in a)]

print()

a = [1,2,3,4]
for i in a[:]:
    a.remove(i)
    print(a)

a = [1,2,3]
b = [1,2]

print(len(set(a) & set(b)))

if 1 != 0: print("IN")

a = 'aabaca'
b = [i for i in a]
print(b)
b.remove(0,'a')
print(b)

l = [1,2,3]
l = []
print(l)

HEAPQ
import heapq

A = [7,2,8,1,0,9]
heapq.heappush(A,11)
heapq.heapify(A)

heapq.heappop(A)
heapq.heappop(A)
print(A)
pq = [-x for x in A]

heapq.heappushpop(A,-199)

print(pq)
heapq.heapify(pq)

print(pq)
heapq.heappop(pq)
print(pq)
for i in range(len(A) - 1):
    x, y = -heapq.heappop(pq), -heapq.heappop(pq)
    print(x,y)
    heapq.heappush(pq, -abs(x - y))
-pq[0]


a = [1,2,3,1,2,1]
print(sorted(set(a)))

a = {1}
a = a | {1}
print(a)

print({i for i in range(8)})
print(list(i for i in range(8)))

a = "abc"
print(a*4)

path = [[1,2],[2,3],[3,1]]

for x, y in path:
    print(x,y)

print(list({1,2,3,4}-{0,1,4})[0])

a = set()
a.add(2)
a.add(3)
print(list(a))

a = [[]]
print(len(a))


print([1,2] - [1,3])

x,y,z = [1,2,3]
print(y)

a = [1,2,3,4,5]
b = [2,3,4,6,8,9]

i1 = 0
i2 = 0
r = []

while True:
    if i1 < len(a) and i2 < len(b):
        if a[i1] < b[i2]:
           r.append(a[i1])
           i1 += 1

        elif b[i2] < a[i1]:
            r.append(b[i2])
            i2 += 1
        else:
            r.append(a[i1])
            r.append(b[i2])
            i1 += 1
            i2 += 1

    elif i1 < len(a) and i2 >= len(b):
        r = r + a[i1:]
        break

    else:
        r = r + b[i2:]
        break

print(r)

# #EXTEND: extend helps to add the all iterable at once to the existing list
a.extend(b)
a.sort()
print(a)
a = set([2,3,4,4])


print(a)

a = str((1,3,4))

print()

a = ["[1]", "[2]"]
# c = ' '.join(a)
# print(c)

print([1,2,3]+[1,2])

lst = [9,12,3,0,0,1,3]
lst.reverse()
a = [1]

[a.insert(0,i) if a[-1] < 9 else a.insert(0,12) for i in lst]

print([4]*0 + [3,2])
a = [5,2,3,32,1]
for i, x in enumerate(a):
    print(i,x)

a = [1,0,1,1]
# a.extend([1,2,3,4])
print(a[1::-1] + a[2:])
# print(a[::-1])

map(lambda x: x if x != 1 else continue, range(4))
#CONVERT FROM BINARY TO DECIMAL
# print(int("011",2))

# print((reduce(lambda accu,val: accu + str(val), a, "4")))
#DEFAULT DICTIONARY
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(list)

#SETDEFAULT in DICTIONARY ==> once store the key and value pair, the value of the stored key will never change with the new value of the same key in future
#if value don't provide the default will be None
a = {}
a.setdefault(2,"ram")
a.setdefault(2,"HARI")
a.setdefault(2,"HARI")
a.setdefault(2,"HARI")
a.setdefault(3,"HARI")
a.setdefault(4)
a.setdefault(4,"Four")
print(a)

for k, v in s:
    d[k].append(v)
print(d.items())

a = [1,2,3,1,2,3]

d = collections.defaultdict(list)

for i,val in enumerate(a):
    d[val].append(i)

print(d)

def heightChecker(self, heights: List[int]) -> int:
    s = sorted(heights)
    return sum([1 for i in range(len(heights)) if s[i] != heights[i]])
a = [1,2,3,4]
print(''.join(a))

a = "a c v c"
print(a.split(" "))

a = [1,2,1,2,2,3]
# a.remove(3)
# print(list(reversed(a)))

c = collections.Counter(a)
c[1] = c[1]-1
print(c[1])
c = c.most_common()
for x,y in c:
    print(x,y)


s = set(a)
s.difference_update([1,2])

print(s)


for i,j in enumerate("abc"):
    print(i,j)

s = set()
s.add('a')
s.add('b')
s.remove('aa')

print(s)

A = [1,0,1,0]
print(5 ^ A[0])
l = list(map(lambda x,y:x+y,a,0))
print(l)
print(5.0 == 5)

a = [6,1,1,13,-1,0,-10,20]
l = [sum(a[:i+1]) for i in range(len(a))]
print(l)

# print(float('inf'))
import sys

print(sys.maxsize)


l.insert(1,22)
l.insert(3,23)
print(l)

import itertools

print([list(perm) for perm in itertools.permutations(l)])

print(l[1:])


import math
print(math.floor(121212/10))

l = [[1,2],[1,3],[2,3]]
s = set([12,1,1])
s.remove(1)

print("abc"*4)

c = reduce(lambda x,y: x * y, l)
print(c)

print(abs(-32))
q,r = divmod(123,10)
print(q,r)

l = [1,2,3,4,1,2,3,4,5,8]
import queue
a = queue.PriorityQueue() #the default one is to get the lowest item first, to get highest item first, do -ve(to the value)
a.put(1)
a.put(12)
a.put(10)
a.put(2)

print(a.get())
print(a.get())
print(a.get())

dic = collections.defaultdict(list)


for i in l:
    dic[i].append(i)

print(dic)

print(''.join(sorted("mint")))


print(list(dic.items()))

print(dic)

c = all([i > 2 for i in l])
print(c)

print(all([True, False]))
print(any([True, False]))

print(bin(18))

print(max(12121,2,4))
print(min(12121,2,4))

#DASH INFRONT OF VARIABLE IN CLASS MEANS A PRIVATE VARIABLE

# print("("*2)

#OPEN FILE
# f = open('/Users/RamYadav/Desktop/a.txt').read()
# for i, j in enumerate(f):
#     print(i)
# print(f.read())

# print(f.split("\n"))
# import time
# for i in range(4):
#     print(time.sleep(1))


#NEXT AND ITER ==> to use next, must create iter object using iter, next just print one item at a time unlike for loop
print(l)
i = iter(l)
print(next(i))
print(next(i))
print(next(i))

l = []
l.append([1,2,3])
l.append([5,6])
print(l)

print("Hello World")
with open('/Users/RamYadav/Desktop/a.txt') as file:
    # for i in file:
    #     print(i)
    #
    a = file.read()

    # for i in a:
    #     print(i)

for i in range(2,5):
    print(i)


a = 'avc mun'
b = a.split(" ")
print(b)


print([99]+[1,2,3])
r = [[]]
for i in [1,2,3]:
    r += [item+[i] for item in r]
#     print(r)
#

# print(reduce(lambda x, l: x + [item+[l] for item in x], [1,2,3],[[]]))

#NOTE: for list 'p' NEVER DO p += 2, this p points to the same address, instead do temp = p + 2
p = []
print(id(p))
p += [2]
print(id(p))
p = p + [2]
print(id(p))

i = 1
print(id(i))
m = i + 1
print(id(m))

print(id(i))
i += 1
print(id(i))

print(i)
# print(m)


# print(list(reversed("abc")))
import itertools
a = "abc"
v = ["".join(i) for i in itertools.permutations(a)]
a = set()
a.update(v)
a.update(["acsd","asdfasdssdf"])
print(a)

b = set(["123",'1212','1212'])

print(a|b)



a = set(itertools.permutations("abc",3))
print(a)

tiles = "abc"
perm = set()
for i in range(1, len(tiles) + 1):
    perm |= set(itertools.permutations(tiles, i))
print (perm)

import collections
collections.deque()

# l = [(1,2,3),(4,5,6)]
# print(l[0][2])

a = (1,2,3,4)
b = collections.Counter(a)
# print(1 in b)

d = collections.defaultdict(list)

a = [1,2,3,4,1,2,3]

for i in a:
    d[i].append(i)

# print(d)
a = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]


a = a[::-1]

# print(a)
# r = [[],[]]
# print(len(r[-2]))

# for i in [4,5]:
# # #     print(i)

# import queue
# q = queue.PriorityQueue()
# q.put(-4)
# q.put(-100)
# q.put(-5)
#
# print(q.get())

# import heapq
# a = [1,2,34,6]
# h = heapq.heapify(a)
# print(heapq.heappop(a))


# import itertools
# temp = [1]*2 +[0]*2
#
# print(list(itertools.permutations("110")))

# import math
# print(math.factorial(9)/math.factorial(7) //math.factorial(2))

# lst = [[1,2,3]]*2
# print(lst)


# x = [[1 for _ in range(5)] for _ in range(6)]
# print(x)



# l = [[1]*3]*5
# print(l)
#RANDOM

# a = [2,3,4]
# print(a[:4])
# import random
# a = [1,2,3,4]
# (random.shuffle(a))#shuffle the list
# # print(a)
# print(random.randrange(1,4))
# print(random.choice([1,4,5,6]))


# for i in range(0,6,2):
#     print(i)
#
#
# for i in (0,6,2):
#     print(i)


# print('9' <= '18')

# def a(i):
#     if i < 2: return True
#     else: return False
#
# print(all([a(i) for i in [1,2,3] ]))

# board = [[1,2,3],[4,5,6],[7,8,9]]
# print(list(zip(*board)))

# s = set()
# s.add(4)
# s.add(5)
# s.remove(9)

# print(16**0.5)



# 12 << n (multiply 12 by 2^n)and  (12 >> n) (divide 12 by 2^n)
# print(1 << 3)

A = [1,2]
B = [3,4,5]

#SHOCKING==> usually from left to right, loop goes from outer to inner
#BUT ==> with [], loop inside [] is inner and right most is outer
# dp = [[0 for _ in range(3)] for _ in range(2)]
#
# b = []
# for i in range(2):
#     a = []
#     for _ in range(3):
#         a.append(0)
#     b.append(a)
#
# print(dp)
# print(b)


# a = set()
#
# print(a)

# from collections import deque
# #
# # queue = deque()
# # queue.append(1)
# # queue.append(2)
# #
# # print(queue.popleft())

#WRITE IN THE SECOND LINE
# print("q" and \
#       "sd")

# a = ["flower","flow","flight"]
#
# print(*a)
#
# print(list(zip(*("flower"))))

# a = [[1,2],[2,1],[3,4],[5,6]]
#
# for i in a:
#     print(sorted(i))

# a = []
# b = [1,2,3,4]
# a = b[:]
# b[1] = 32
# print(a)

# points = [[1,3],[-2,2]]
# dic = {}
# for x, y in points:
#     val = x ** 2 + y ** 2
#     dic[val] = [x,y]
#
# a = [1,2,3,4]
# print(a[::-1])

# points = [[1,3],[-2,2]]
# K = 1
#
# import heapq
# heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)

# a = "awaglk"
# k = 4
# l = []
#
# i = a[:k]
# l.append(i)
#
# for j in range(k,len(a)):
#     i = i[1:]+ a[j]
#     l.append(i)
#
#
# for i in l:
#     s = set(i)
#     if len(s) == len(i)-1: print(i)


# movie_duration = [90, 85, 75, 60, 120, 150, 125]
# d = 250-30
#
# dic = {}
#
# for i in range(len(movie_duration)-1):
#     for j in range(i+1, len(movie_duration)):
#         if movie_duration[i] + movie_duration[j] <= d: dic[movie_duration[i] + movie_duration[j]] = [movie_duration[i], movie_duration[j]]
#
#
# r = [i for i in dic.keys()]
# r.sort()
# r = r[::-1]
# print(r)


# maxTravelDist = 10,000
# forwardRouteList = [[1,3000],[2,5000],[3,7000],[4,10000]]
# returnRouteList = [[1,2000],[2,3000],[3,4000],[4,5000]]

# a = set()
# a.add((3,4))
# print(a)
#
# b = [1,2]
# print(tuple(b))

# A = [[1,2],[2,1],[3,4],[5,6], [1,2]]
#
# d = collections.Counter(tuple(i) for i in A)
# print(d.values())
#
# print([v*(v-1)/2 for v in d.values()])
#
# import math
# print(sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(x)) for x in A).values()))
# sum(v * (v - 1) // 2 for v in collections.Counter(tuple(sorted(i)) for i in A).values())


# print(round(3)) #round number to its upper when .5 and less when it les <.5
# import math
# print(math.ceil(5)) #always round number to its upper level


# start = "RXXLRXRXL"
# end = "XRLXXRRLX"
#
# a = zip(start, end)
#
# for x,y in a:
#     print([x,y])

from collections import deque

# x = deque()
# x.append(1)
# print(x)


# a = (5,6)
# print(a)


# for x,y in [[3,5]]:
#     print(x,y)


# movie_duration = [90, 85, 75, 60, 120, 150, 125]
# d = 250-30
#
# movie_duration.sort()
#
# dic = collections.defaultdict(list)
#
# start = 0
# end = len(movie_duration)-1
#
# while start < end:
#     cur = movie_duration[start] + movie_duration[end]
#     dic[cur].append((movie_duration[start], movie_duration[end]))
#     if cur > d: end -= 1
#     else: start += 1
#
# c = 0
#
# for val in dic.keys():
#     if c < val and val < d: c = val
#
# print(dic[c])



#MAKE A 2D GRAPH
# graph = [[0 for column in range(4)] for row in range(3)]
# print(graph)
#
# l = []
#
# for i in range(3):
#     for j in range(4):
#         l.append((i,j))
#
# print(l)
#
# print([(i,j) for i in range(3) for j in range(4)]) #this is different than previous (graph)

# a = "this is most common"
#
# import string
# print(string.punctuation)
# a = a.split(" ")
# d = collections.Counter(a)
#
# print(d)

#SINGLE STAR AND DOUBLE STAR infront of variable
#The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions
#The *args will give you all function parameters as a tuple:
# def foo(*args):
#     for i in args:
#         print(i)
#
# foo(1)
# foo(1,2,3,4)

#The **kwargs will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary.

# def foo(**kwargs):
#     for i in kwargs:
#         print(i, kwargs[i])
#
# foo(name=1 ,names=2)


# a = [1,2,3,4,5]
# print(a[:1])

# str = "awaglknagawunagwkwagl"
# k = 4
#
# r = set()
#
# for i in range(len(str)-4):
#     r.add(str[i:i+4])
#
# ans =  [i for i in r if len(set(i)) == len(i)]
# print(ans)

import string
# print(string.punctuation)

a = "MNdojid, !!sdfsfdf"
# a = a.replace(",", "")
# print(a)

# print(a.lower())

# for i in string.punctuation:
#     a = a.replace(i,"")
# print(a)
#
#SORT
'''
list_name.sort() – it sorts in ascending order
list_name.sort(reverse=True) – it sorts in descending order
list_name.sort(key=…, reverse=…) – it sorts according to user’s choice

'''
#DELETE DECTIONARY ITEM WITHOUT ANY ERROR, put None
# dic = collections.Counter(a)
# dic.pop('dd',None)
# print(dic)

#If want to split from the space, must put at least one space, having more than one space wouldn't effect the splitting
#but must not specify how to split it
# a  = "a, a, a,           a,              b,b,b,c, c"
# #
# # for i in string.punctuation:
# #     a = a.replace(i," ")
# # print(a)
# # a = a.split()
# #
# # print(a)

# a = ['a','b']
# a.remove(a[-2])

A = [1, 6, 2, 3]
A = [1,1,6]

cnt = collections.Counter(A)
print(min(2*cnt[7-i]+len(A)-cnt[7-i]-cnt[i] for i in range(1,7)))