#treenode
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

def pre_order(root):
    if not root:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)
    
def post_order(root):
    if not root:
        return
    
    post_order(root.left)
    post_order(root.right)
    print(root.value)
print("pre")
pre_order(root)
print("post")
post_order(root)

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)

print("in")
in_order(root)