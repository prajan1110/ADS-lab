class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Doubly_LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def traverse_forward(self):
        if self.is_empty():
            print("The list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.value, end=" " if temp.next else "\n")
            temp = temp.next

    def delete_node(self, value):
        if self.is_empty():
            print("List is empty, nothing to delete.")
            return

        temp = self.head

        if temp is not None and temp.value == value:
            if temp.next is None:
                self.head = None
            else:
                self.head = temp.next
                self.head.prev = None
            print(f"Deleted node with value {value}")
            return

        while temp is not None and temp.value != value:
            temp = temp.next

        if temp is None:
            print(f"Node with value {value} not found.")
            return

        if temp.next is None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

        print(f"Deleted node with value {value}")


dll = Doubly_LinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
    
print("Doubly Linked List after creation:")
dll.traverse_forward()

dll.delete_node(10)  
dll.traverse_forward()

dll.delete_node(30)  
dll.traverse_forward()

dll.delete_node(40)  
dll.traverse_forward()

dll.delete_node(100)  