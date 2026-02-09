class Node():
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class Doubly_LinkedList():
    def __init__(self):
        self.head = Node(None,None,None)
        
        self.Node1 = Node(10,None,None)
        self.Node2 = Node(11,None,None)
        self.Node3 = Node(12,None,None)

        self.Node1.next = self.Node2
        self.Node2.prev = self.Node1
        self.Node2.next = self.Node3
        self.Node3.prev = self.Node2

        self.head.next = self.Node1
        self.Node1.prev = self.head

    def traverse_forward(self):
        temp = self.head
        while (temp != None):
            print(temp.value)
            temp = temp.next
        print()
    
    def traverse_backward(self):
        temp = self.head
        while (temp.next != None):  
            temp = temp.next
            
        while (temp != None):
            print(temp.value)
            temp = temp.prev
        print()
        
n1=Doubly_LinkedList()
n1.traverse_forward()
n1.traverse_backward()