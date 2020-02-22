#########################
###### LINKED LIST ######
#########################
class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def addValue(self,value:int):
        if not self.head:
            self.head = Node(value)
            self.length += 1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = Node(value)
            self.length += 1

    def list_print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def size(self):
        return self.length

    def clear(self):
        self.__init__()

#NOTE: I have created list in every questions
# 1 Remove Dups
l = LinkedList()
l.addValue(1)
l.addValue(2)
l.addValue(8)
l.addValue(1)
l.addValue(2)
l.addValue(8)

# l.list_print()
def revmoveDup(head):
    temp = head
    s = set()
    while temp.next:
        s.add(temp.val)
        if temp.next.val in s:
            temp.next = temp.next.next
        else: temp = temp.next
revmoveDup(l.head)
# l.list_print()

#Note:==>if temp buffer like set is not allowed, then first needs to be sorted and then compare one to next as go in the loop


#2 Return kth to Last
l = LinkedList()
l.addValue(1)
l.addValue(2)
l.addValue(3)
l.addValue(4)
l.addValue(5)
l.addValue(6)

l.list_print()
print(l.size())
def kthToLast(kth:int): #solution I
    if kth > l.size() or kth <= 0: return -1
    count = 6
    temp = l.head
    while count >= 0:
        if kth == count: return temp.val
        temp = temp.next
        count -= 1

def recurKthToLast(head, kth:int,count): #solution II
    if kth == count: return head.val
    return recurKthToLast(head.next,kth,count-1)


print(recurKthToLast(l.head,2,6))
print(kthToLast(2))


#3 Delete Middle Node
l = LinkedList()
l.addValue(1)
l.addValue(2)
l.addValue(3)
l.addValue(4)
l.addValue(5)
l.addValue(6)
# l.list_print()

temp =l.head.next.next #giving only the deleting node, which is 3
# print(temp.val)
def deleteMiddleNode(node):
    temp.val = temp.next.val
    temp.next = temp.next.next

deleteMiddleNode(temp)
l.list_print()

4 Partition
l = LinkedList()
l.addValue(3)
l.addValue(5)
l.addValue(8)
l.addValue(5)
l.addValue(10)
l.addValue(2)
l.addValue(1)
# l.list_print()

def helper(head):
    temp = l.head
    lst = []
    while temp:
        lst.append(temp.val)
        temp = temp.next

    head = None
    lst.sort()
    lst.reverse()
    return lst

lst = helper(l.head)

def partition(lst):
    head = None
    t = None
    while lst:
        if not head:
            val = lst.pop()
            head = Node(val)
            t = head
        else:
            val = lst.pop()
            t.next = Node(val)
            t = t.next
    return head

head = partition(lst)
#printing result
while head:
    print(head.val)
    head = head.next




#5 Sum Lists

l1 = LinkedList()
l1.addValue(7)
l1.addValue(1)
l1.addValue(6)
# l1.list_print()

l2 = LinkedList()
l2.addValue(5)
l2.addValue(9)
l2.addValue(2)

# l2.list_print()

h1 = l1.head
h2 = l2.head

def sumLists(h1:Node, h2:Node):
    head = None
    q,r = 0,0
    temp = None

    while h1 or h2:
        v1 = 0 if not h1 else h1.val
        v2 = 0 if not h2 else h2.val
        q,r = divmod(v1+v2+q,10)

        if h1: h1 = h1.next
        if h2: h2 = h2.next

        if not head:
            head = Node(r)
            temp = head
            temp.next = None
        else:
            temp.next = Node(r)
            temp = temp.next
            temp.next = None
    return head

head = sumLists(h1,h2)
while head:
    print(head.val)
    head = head.next

For reverse, just reverse all lists with answers, below reversed the answer

def reverse(answer:Node):
    prev = None
    cur = head

    while cur:
        temp = cur
        cur = cur.next
        temp.next = prev
        prev = temp
    return prev

head = reverse(head)
while head:
    print(head.val)
#     head = head.next




#6 Palindrome
l1 = LinkedList()
l1.addValue(1)
l1.addValue(2)
l1.addValue(1)

def checkPalindrom(head:Node):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next

    return lst == lst[::-1]

print(checkPalindrom(l1.head))



#7 Intersection (Intersection by value)
l1 = LinkedList()
l1.addValue(7)
l1.addValue(1)
l1.addValue(5)
# l1.list_print()

l2 = LinkedList()
l2.addValue(5)
l2.addValue(9)
l2.addValue(2)

def intersectionByValue(h1:Node, h2:Node):
    l1 = []
    l2 = []
    while h1:
        l1.append(h1.val)
        h1 = h1.next

    while h2:
        l2.append(h2.val)
        h2 = h2.next

    return set(l1)&set(l2)

print(intersectionByValue(l1.head,l2.head))


#8 Loop Detection by Value (would be similar technique with node)
l1 = LinkedList()
l1.addValue(7)
l1.addValue(1)
l1.addValue(5)
l1.addValue(17)
l1.addValue(1)
l1.addValue(9)
# l1.list_print()

def loopDetection(head:Node):
    s = set()
    while True:
        if head.val in s: return head.val
        s.add(head.val)
        head = head.next

print(loopDetection(l1.head))