class Node:
    def __init__(self, value,head):
        self.value = value
        self.next = None

class traverse_list:
    def __init__(self):
        self.head = None

    def print_node(head):
        temp = head
        while (temp):
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def linked_list(head, search_value):
        temp = head
        while (temp):
            if (temp.value == search_value):
                print(search_value, 'found')
            temp = temp.next
        print(search_value,'not found')

n1 = Node(2,None)
n2 = Node(3,None)
n3 = Node(4,None)
n4 = Node(5,None)
n5 = Node(6,None)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

search_value = int(input("Enter the value to search: "))
print("The traversing list is:")
traverse_list.print_node(n1)

print(traverse_list.linked_list(n1, search_value))
