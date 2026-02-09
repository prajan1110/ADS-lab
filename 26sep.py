# Create a class node that has the following attributes:
# value, next, prev

# Create a class doubly_linkedlist and include the following operations:
# Creation of a doubly linked list with five nodes
# Write a method to make a doubly linked list circular
# Write a method to find the middle element in a doubly linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class Doubly_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
       
    def insert_node(self,value):
        if not self.head:
            self.head=Node(value)
            self.tail=self.head       
        else:
            new=Node(value)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
            return      

    def begin_add(self,value):
        if not self.head:
            self.head=Node(value)
            self.tail=self.head
        else:
            curr=Node(value)
            curr.next=self.head
            self.head.prev=curr
            self.head=curr
            return
    def foward_travers(self):
        if not self.head:
            print("Empty List")
        else:
            curr=self.head
            while curr:
                print(curr.value)
                curr=curr.next
            print('None')   
    
    def backward_traverse(self):
        if not self.head:
            print("Empty List")
        else:
            curr =self.tail
            while curr:
                print(curr.value)
                curr =curr.prev
    def delete_node(self,value):
        if not self.head:
            print("Empty list")
        else:
            if self.head.value==value:
                if not self.head.next:  
                    self.head=None
                    self.tail=None
                    return
                self.head=self.head.next
                self.head.prev=None
                return
            elif self.tail.value==value:
                self.tail.prev.next=None
                temp=self.tail.prev
                self.tail.prev=None
                self.tail=temp
                return
            else:
                curr=self.head
                prev=None
                while curr.next:
                    if curr.value==value:
                        curr.next.prev=prev
                        prev.next=curr.next
                        break
                    prev=curr
                    curr=curr.next
                print("value Not found")

    def create_circular_node(self):
        if not self.head:
            print("Empty list")
        else:
            self.tail.next=self.head
            self.head.prev=self.tail
    def print_circular(self):
        if not self.head:
            print("Empty list")
        else:
            curr=self.head
            print(self.head.prev.value)

            while curr is not self.tail:
                print(curr.value)
                curr=curr.next
            print(self.tail.value)
            print(self.tail.next.value)
    def print_middle(self):
        if not self.head:
            print("Empty list")
        else:
            l1=[]
            curr=self.head
            while curr is not self.tail:
                l1.append(curr.value)
                curr=curr.next
            l1.append(self.tail.value)
            print(l1[len(l1)//2])

dl=Doubly_linked_list()
dl.insert_node(12)
dl.insert_node(11)
dl.insert_node(10)
dl.begin_add(1)
dl.delete_node(20)
print("Delete:")
dl.foward_travers()

print("Backward traversing:")
dl.backward_traverse()

print("Circular:")
dl.create_circular_node()
dl.print_circular()

print("Middle node:")
dl.print_middle()
