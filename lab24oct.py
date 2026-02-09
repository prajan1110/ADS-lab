#Generic
class trees():
    def __init__(self,value):
        self.value=value 
        self.left=None 
        self.right=None 

def create_bin(arr,i,n):
    if i<n:
        temp=trees(arr[i])
        root=temp
        root.left=create_bin(arr,2*i+1,n)
        root.right=create_bin(arr,2*i+2,n) 
        return root 
    return None

def inorder(root):
    if not root:
        return
    
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preorder(root):
    if not root:
        return 
    
    print(root.value)
    preorder(root.left)
    preorder(root.right)
    
def postorder(root):
    if not root:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.value)


arr=[11,12,13,14,15,16,17,18]
n=len(arr)
root=create_bin(arr,0,n)

print("inorder")
inorder(root)

print("preorder")
preorder(root)

print("postorder")
postorder(root)

#specific
class trees:
    def __init__(self,value):
        self.value=value 
        self.left=None 
        self.right=None 

t=trees(11)
t.left=trees(12)
t.right=trees(2)
t.left.left=trees(1)
t.left.right=trees(4)
t.right.left=trees(3)
t.right.right=trees(10)
def preorder(root):
    if not root:
        return 
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)

def post_order(root,s=""):
    if not root:
        return
    post_order(root.left,"-->l")
    post_order(root.right,'-->r')
    print(root.value,s)

def in_order(root):  
    if not root:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)
preorder(t)
post_order(t)
in_order(t)