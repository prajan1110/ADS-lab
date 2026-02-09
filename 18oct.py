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
root.right.left=Node(13)
root.right.right=Node(14)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
root.left.right.left=Node(10)
root.left.right.right=Node(11)
root.right.left.right=Node(15)
root.right.right.left=Node(18)
root.right.right.right=Node(19)
root.left.left.right.left=Node(8)
root.left.left.right.right=Node(9)
root.left.right.right.left=Node(12)
root.right.left.right.left=Node(16)
root.right.left.right.right=Node(17)
root.right.right.right.left=Node(20)








def post_order(root):
    if not root:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.value)
print("post")
post_order(root)