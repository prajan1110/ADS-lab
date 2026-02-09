#bfs
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
t = Node(1)
t.left = Node(10)
t.right = Node(12)
t.left.left = Node(13)
t.left.right = Node(24)
t.right.left = Node(55)
t.right.right = Node(76)

def bfs(root):
    if not root:
        return

    q = [root]

    while q:
        node = q.pop(0)
        print(node.value,end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
bfs(t)