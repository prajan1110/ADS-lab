# Write a program to create a class/structure Node to represent a node in a singly linked list. Each node shouit have two attributes: data and next. Then, create a class/structure Stack to represent the stack itsell Implement the following operations:

# 1.peek(): Return the data of the top node without removing it. If the stack is empty, return None. 2.. is_empty(): Return True if the stack is empty, otherwise return False

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Stack():
    def __init__(self):
        self.head=None
        
    def is_empty(self):
        if (self.head is None):
            print("Stack is empty")
            return True
        else:
            print("Stack is not empty")
            return False
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Can't pop, if stack is empty")
            return None
        pop_value = self.head.value
        self.head = self.head.next
        return pop_value
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty,no element is there to peek.")
            return None
        return self.head.value

    def print_stack(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            temp = self.head
            elements = []
            while temp:
                elements.append(temp.value)
                temp = temp.next
            return elements
s1=Stack()

s1.push(12)
s1.push(2)
s1.push(11)
s1.push(1)
s1.push(10)

stack_elements_before = s1.print_stack()
print("Stack before popping:", stack_elements_before)

popped_element = s1.pop()
print("Popped element:", popped_element)

stack_elements_after = s1.print_stack()
print("Stack after popping:", stack_elements_after)

print("Top element (peek):", s1.peek())


# Write a programata and next. Then, dato represent a node in a singly linked list. Each node should have we attributes operations ext. Then, create a class/structure Queueinked list ach node should have the following

# 1. dequeue(): Remove and return the front node from the queue. If the queue is empty, return None.
class Node():
    def __init__(self,value,next):
        self.value=value
        self.next= next

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
        
    def is_empty(self):
        if (self.front == None and self.rear == None):
            print("The queue is empty")
            return True
        else:
            print("The queue is not empty")
            return False
        
    def enqueue(self,value):
        new_node=Node(value,None)
        if (self.front == None and self.rear == None):
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print_queue(self):
        if (self.front == None and self.rear == None):
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print()
            
    def dequeue(self):
        if (self.front == None and self.rear == None):
            print("Can't remove from an empty queue")
        else:
            deleted_value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return deleted_value
        


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.print_queue()  

q.dequeue()       
q.print_queue() 
 