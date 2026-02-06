# Create a class node with the following attributes : value, next
# Create a class Stack and the class Stack should have the following methods:
# init()
# is_empty(): that checks whether the stack is empty or not
# pop(): pop the topmost element into the stack
# print():print the stack

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
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
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Cannot pop, stack is empty")
            return None
        pop_value = self.head.value
        self.head = self.head.next
        return pop_value

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

n1 = Stack()

n1.push(11)
n1.push(12)
n1.push(13)

stack_elements_before = n1.print_stack()
print("Stack before popping:", stack_elements_before)

popped_element = n1.pop()
print("Popped element:", popped_element)

stack_elements_after = n1.print_stack()
print("Stack after popping:", stack_elements_after)
