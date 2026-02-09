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

def evaluate(expression):
    stack = Stack()  

    for char in expression.split():
        if char.isdigit():  
            stack.push(int(char))
        else:  
            right_operand = stack.pop()
            left_operand = stack.pop()

            
            if char == '+':
                result = left_operand + right_operand
            elif char == '-':
                result = left_operand - right_operand
            elif char == '*':
                result = left_operand * right_operand
            elif char == '/':
                result = left_operand / right_operand  

            stack.push(result)

    return stack.pop()

expression = "5 6 2 + * 12 4 / -"
result = evaluate(expression)
print("The result of the expression ",expression, "is:" ,result)
