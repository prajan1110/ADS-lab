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
        
    def insert(self,value):
        new_node=Node(value,None)
        if (self.is_empty()):
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print_queue(self):
        if (self.is_empty()):
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print()
            
    def delete(self):
        if self.is_empty():
            print("Cannot remove from an empty queue")
        else:
            deleted_value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return deleted_value

q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
q.print_queue()  

q.delete()       
q.print_queue() 

        