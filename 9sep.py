#append node and delete node
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = None

    def print_node(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print("None")

    def append_node_end(self, new_value):
        new_node = self.create_node(new_value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_node_begin(self, new_value):
        new_node = self.create_node(new_value)
        new_node.next = self.head
        self.head = new_node

    def create_node(self, value):
        return Node(value)

    def append_node_position(self, new_value, position):
        new_node = self.create_node(new_value)
        if position == 0:
            self.append_node_begin(new_value)
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
        
    def delete_node_by_value(self, value):
        current = self.head
        if not current:
            print("List is empty.")
            return
        if current.value == value:
            self.head = current.next
            return
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        if current is None:
            print("Value not found.")
            return
        prev.next = current.next 
        
    def delete_node_by_position(self, position):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        if position == 0:
            self.head = current.next  
            return
        prev = None
        count = 0
        while current and count != position:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("Position out of range.")
            return
        prev.next = current.next

linked_list = Linked_List()

linked_list.append_node_end(1)
linked_list.append_node_end(2)
linked_list.append_node_end(3)
linked_list.append_node_end(4)
linked_list.append_node_end(5)

print("Original list:")
linked_list.print_node()

linked_list.append_node_end(6)
print("List after appending  at the end:")
linked_list.print_node()

linked_list.append_node_begin(0)
print("List after appending  at the beginning:")
linked_list.print_node()

position = int(input("Enter the position where you want to append : "))
linked_list.append_node_position(8, position)
print("List after appending at position", position,":")
linked_list.print_node()

value_to_delete = int(input("Enter the value you want to delete: "))
linked_list.delete_node_by_value(value_to_delete)
print("List after deleting value" ,value_to_delete,":")
linked_list.print_node()

position_to_delete = int(input("Enter the position you want to delete: "))
linked_list.delete_node_by_position(position_to_delete)
print("List after deleting node at position" ,position_to_delete,":")
linked_list.print_node()
