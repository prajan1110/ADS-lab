#Create a class Node with attributes
# value, next
# Create five nodes and link them.
# Perform the following operations:
# Print the list
# Insert a new node at the end of the list
# Insert a new node at the beginning of the list
# Insert a new node at a specific position in the list(the position has to be given by the user)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print("None")

    def insert_at_end(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, new_value, position):
        new_node = Node(new_value)
        if position == 0:
            self.insert_at_beginning(new_value)
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

linked_list = Linked_List()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)

print("Original list:")
linked_list.print_list()

linked_list.insert_at_end(6)
print("List after inserting 6 at the end:")
linked_list.print_list()

linked_list.insert_at_beginning(0)
print("List after inserting 0 at the beginning:")
linked_list.print_list()

position = int(input("Enter the position where you want to insert 8: "))
linked_list.insert_at_position(8, position)
print(f"List after inserting 8 at position {position}:")
linked_list.print_list()
