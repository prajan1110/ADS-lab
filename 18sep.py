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

#Printer
def printer(queue):
    print("Printer Starting...!")
    while not queue.is_empty():
        job = queue.dequeue()
        print("Printing: ",job)
    print("All jobs have been printed.")
        
q.enqueue("Document A")
q.enqueue("Document B")
q.enqueue("Document C")
    
print("Print Queue:")
q.print_queue()

printer(q)