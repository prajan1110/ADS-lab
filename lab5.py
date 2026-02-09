# Write a program to create a class/structure DoublyNode to represent a node in a doubly linked list. Each node should have three attributes: data, next, and prev. Then, create a class/structure DoublyLinkedList to represent the linked list itself. Implement the following operations:

# ⚫ delete_node(data): Delete the first node in the list that contains the given data.
# ⚫ traverse_backward(): Traverse the list backward and print the data of each node.

class Node():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)  
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def traverse_node(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def traverse_backward(self):
        temp = self.head
        if temp is None:
            print("The list is empty.")
            return

        while temp.next is not None:
            temp = temp.next
        
        while temp is not None:
            print(temp.value)
            temp = temp.prev
    
    def delete_node(self, value):
        if (self.head is None):
            print("List is empty, cannot delete.")
            return

        temp = self.head

        if (temp is not None and temp.value == value):
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            print("Deleted node with value:", value)
            return

        while temp is not None and temp.value != value:
            temp = temp.next

        if (temp is None):
            print("Node with value" ,value ,"not found.")
            return

        if (temp.next is not None):
            temp.next.prev = temp.prev
        if (temp.prev is not None):
            temp.prev.next = temp.next

        print("Deleted node with value: ",value)


n1 = DoublyLinkedList()
n1.insert(10)
n1.insert(20)
n1.insert(30)
n1.insert(40)   
n1.traverse_node()    

print("The List after traversing backward: ")
n1.traverse_backward()

to_delete = int(input("Enter the value of the node to be deleted: "))
n1.delete_node(to_delete)

print("The List after deletion:")
n1.traverse_node()
