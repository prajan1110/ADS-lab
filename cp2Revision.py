# Write a Python program to find the average of all even numbers in  a give list [1,3,4,6,8,10]
li = [1,3,4,6,8,10]

even_numbers = [num for num in li if num%2 == 0]

if even_numbers:
    average = sum(even_numbers)/len(even_numbers)
    print("Average of even numbers: ",average)
else:
    print("No even number in the list.")


# Write a Python program to print the last element of a given singly linked list list 2->3->4->8->9 and check if that element is a multiple of 3
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    temp = head
    while temp.next:
        temp = temp.next
    print("Last element : ",temp.value)
    if temp.value % 3 == 0:
        print(temp.value,"is a multiple of 3")
    else:
        print(temp.value,"is not a multiple of 3")

n1 = Node(2)
n1.next = Node(3)
n1.next.next = Node(4)
n1.next.next.next = Node(8)
n1.next.next.next.next = Node(9)

print_list(n1)

# Create a class complex number with attributes real and imaginary. Define a method to find the sum of a complex number
