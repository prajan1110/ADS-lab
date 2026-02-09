class trees:
    def _init_(self,value):
        self.value=value 
        self.left=None 
        self.right=None 

t=trees(11)
t.right=trees(20)
t.right.left=trees(21)
t.left=trees(11)
t.left.left=trees(8)
t.left.left.right=trees(17)
t.left.right=trees(19)

def postorder(root):
    if not root:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" ")
postorder(t)