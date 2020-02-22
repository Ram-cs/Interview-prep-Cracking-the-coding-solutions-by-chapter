##############################
##### Trees and Graphs #######
##############################


class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value


class BinaryTree:
    def __init__(self):
        self.head = None


    def add(self,value):
        if not self.head: self.head = Node(value)
        else:
            temp = self.head
            while True:
                if value < temp.val:
                    if not temp.left:
                        temp.left = Node(value)
                        return
                    temp = temp.left
                elif value == temp.val: return
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        return
                    temp = temp.right

    def p(self,head):
        if not head: return
        print(head.val)
        self.p(head.left)
        self.p(head.right)


    def print_recursively(self):
        self.p(self.head)

    def print_tree(self):
        import queue
        temp = self.head
        if not temp: return
        queue = queue.deque()
        queue.append(temp)

        while queue:
            p = queue.popleft()
            print(p.val)
            if p.left: queue.append(p.left)
            if p.right: queue.append(p.right)



# bt = BinaryTree()
# bt.add(5)
# bt.add(3)
# bt.add(4)
# bt.add(2)
# bt.add(7)
# bt.add(6)
# bt.add(8)
# bt.print_tree()

# bt.print_recursively()




#1 Route Between Nodes
#Use DFS or BFS to find if two nodes are connected


#2 Minimal Tree
#Created a binary tree above

#3 List of Depths


#4 Check Balanced Tree
# bt = BinaryTree()
# bt.add(5)
# bt.add(3)
# bt.add(4)
# bt.add(2)
# bt.add(7)
# bt.add(6)
# bt.add(8)
#
# # bt.print_tree()
#
# def helper(head: Node):
#     if not head: return True, -1
#     rL,left = helper(head.left)
#     rR,right = helper(head.right)
#     if not rL or not rR or abs(left-right) > 1: return False, 0
#     else: return True, max(left, right)+1
#
# result, p = helper(bt.head)
# print(result) #give true
# #adding more nodes
# bt.add(11)
# bt.add(13)
# result, p = helper(bt.head)
# print(result) #give False




#5 Validate BST
# bt = BinaryTree()
# bt.add(5)
# bt.add(3)
# bt.add(4)
# bt.add(2)
# bt.add(7)
# bt.add(6)
# bt.add(8)
# bt.print_recursively()

# def validateBST(head:Node):
#     import queue
#     queue = queue.deque()
#     if not head: return -1
#     queue.append(head)
#
#     while queue:
#         node = queue.popleft()
#         if node.left:
#             if node.left.val > node.val: return False
#             queue.append(node.left)
#         if node.right:
#             if node.right.val < node.val: return False
#             queue.append(node.right)
#
#     return True
#
# print(validateBST(bt.head))




#6 Successor




#7 Build Order
# import collections
# projects = ['a','b','c','d','e','f']
# dependencies = [('a','b'), ('f','b'),('b','d'),('f','a'),('d','c')]
#
# dic = collections.defaultdict(list)
#
# for p,d in dependencies:
#     dic[p].append(d)
#
# result = list(set(projects)-set(dic.keys()))
# if not len(result): print("Not")
#
# print(dic)


#8 First Common Ancestor



