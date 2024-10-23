class trees():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
def create():
    root=trees(1)
    nodeA=trees(2)
    nodeB=trees(3)
    nodeC=trees(4)
    nodeD=trees(5)
    nodeE=trees(6)
    nodeF=trees(7)
    nodeG=trees(8)
    nodeH=trees(9)
    nodeI=trees(10)
    nodeJ=trees(11)
    nodeK=trees(12)
    nodeL=trees(13)
    nodeM=trees(14)
    nodeN=trees(15)
    nodeO=trees(16)
    nodeP=trees(17)
    nodeQ=trees(18)
    nodeR=trees(19)
    nodeS=trees(20)

    root.left=nodeA
    root.right=nodeB


    nodeA.right=nodeD
    nodeA.left=nodeC

    nodeC.left=nodeE
    nodeC.right=nodeF

    nodeF.left=nodeG
    nodeF.right=nodeH

    nodeD.left=nodeI
    nodeD.right=nodeJ

    nodeJ.left=nodeK

    nodeB.left=nodeL
    nodeB.right=nodeM

    nodeM.left=nodeQ
    nodeM.right=nodeR

    nodeR.left=nodeS

    nodeL.left=nodeN

    nodeN.left=nodeO
    nodeN.right=nodeP
    
    return root
    
    
a=create()

a=create()

def preorder (root):
    if not root :
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
    
    
def postorder(root):
    if not root :
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")

def level_order(root):
    if not root:
        return
    
    queue = [root]  
    while queue:
        current = queue.pop(0)  
        print(current.data, end=" ")  
        
       
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)   
       
print("preorder")    
preorder(a)
print("\n")
print("inorder")
inorder(a)
print("\n")
print("postorder")
postorder(a)
print("\n")
print("levelorder")
level_order(a)