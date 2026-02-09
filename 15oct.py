class trees:
    def __init__(self,value):
        self.value=value 
        self.left=None 
        self.right=None 


def create_bin(arr,i,n):
    if i<n:
        temp=trees(arr[i])
        root=temp
        root.left=create_bin(arr,2*i+1,n)
        root.right=create_bin(arr,2*i+1,n) 
        return root 
    return None

def preorder(root):
    if not root:
        return 
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)


arr=[1,2,4,5,3,7,6]
n=len(arr)
root=create_bin(arr,0,n)
preorder(root)