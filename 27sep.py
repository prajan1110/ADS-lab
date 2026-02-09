class Node():
    def __init__(self,value,next,prev):
        self.value=value
        self.next=None
        self.prev=None
    
class CircularLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    
    def create_node(self):
        self.n1 = Node(10,None,None)
        self.n2 = Node(20,None,None)
        self.n3 = Node(30,None,None)

        self.head = self.n1
        self.tail = self.n3

        self.head.next = self.n2
        self.n2.next = self.tail
        self.tail.next = self.head

        self.head.prev = self.tail
        self.n2.prev = self.head
        self.tail.prev = self.n2

    def print_circular(self):
        if not self.head:
            print("Empty list")
        else:
            temp = self.head
            while True:
                print(temp.value)
                temp = temp.next
                if temp == self.head:
                    break
        
Clist = CircularLinkedList()
Clist.create_node()
Clist.print_circular()
        