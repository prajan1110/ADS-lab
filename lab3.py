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
            new=Node(value)
            new.next=self.head
            self.head=new
            return
    def pop(self):
        if not self.head:
            print("Empty stack")
        else:
            self.head=self.head.next
            return
    def print_stack(self):
        if not self.head:
            print("Empty stack")
        else:
            curr=self.head
            while curr is not None:
                print(curr.value)
                curr=curr.next
s1=Stack()
s1.push(3)
s1.push(7)
s1.push(5)
s1.pop()
s1.print_stack()
l1=[]
l1.insert(0,3)
l1.insert(0,6)
l1.insert(0,1)
l1.insert(0,7)
l1.insert(0,9)
l1.pop(0)
print(l1)