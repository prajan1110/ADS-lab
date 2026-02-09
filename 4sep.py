##
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        
n1 = Node(2)
print(n1.value, n1.next)

##
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        
n1 = Node(2)
n2 = Node(3)
n1.next = n2

print(n1.value, n1.next.value)
