class Node():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Doubly_LinkedList():
    def __init__(self):
        self.head = None
      
    def insert_at_beginning(self,value):
        new_node = Node(value)
        if (self.head == None):
            self.head=new_node 
        else:
            new_node.next=self.head 
            self.head.prev=new_node
            self.head=new_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def traverse_forward(self):
        temp = self.head
        while (temp != None):
            print(temp.value)
            temp = temp.next
        print()
    
    def traverse_backward(self):
        temp = self.head
        if temp is None:
            return  

        while (temp.next != None):  
            temp = temp.next
            
        while (temp != None):
            print(temp.value)
            temp = temp.prev
        print()
        
n1=Doubly_LinkedList()
n1.insert_at_beginning(12)
n1.insert_at_beginning(2)
n1.insert_at_beginning(11)
n1.insert_at_beginning(1)
n1.traverse_forward()
n1.traverse_backward()

n1.insert_at_beginning(10)
n1.traverse_forward()

n1.insert_at_end(20)
n1.traverse_forward()



