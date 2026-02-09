class Node():
    def __init__(self, value, next=None): 
        self.value = value
        self.next = next

class Stack():
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        if self.head is None:
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False
    
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def print_stack(self):
        if self.head is None:
            print("Stack is empty")
            return
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.value)
                tmp = tmp.next
                print()

n1 = Stack()

n1.push(11)
n1.push(12)
n1.push(13)
n1.print_stack()
