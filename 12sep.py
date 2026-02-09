# 1. Implement a stack using a singly linked list in Python with the following operations:
# Push : Add an element to the top.
# Pop : Remove and return the top element.
# Traverse : Display all elements from top to bottom.
# 2. Implement a stack using list
class Node: 
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=None
        
    def push(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
            return
        
    def pop(self):
        if not self.head:
            print("Stack is empty")
        else:
            self.head=self.head.next
            return
        
    def print_stack(self):
        if not self.head:
            print("Stack is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.value)
                temp=temp.next
s1=Stack()
s1.push(2)
s1.push(5)
s1.push(8)
s1.push(1)
s1.print_stack()

s1.pop()
s1.print_stack()

l1=[]
l1.insert(0,3)
l1.insert(0,6)
l1.insert(0,2)
l1.insert(0,4)
l1.insert(0,9)
print(l1)

l1.pop(0)
print(l1)