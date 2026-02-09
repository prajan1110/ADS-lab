#lca

class treeNode:
    def _init_(self,value):
        self.value=value
        self.right=None
        self.left=None
def create():
    root=treeNode(3)
    root.left=treeNode(9) 
    root.right=treeNode(6)       
    root.left.left=treeNode(7)
    root.left.right=treeNode(8)
    root.right.left=treeNode(5)
    root.right.right=treeNode(4)
    root.left.right.left=treeNode(2)
    root.left.right.right=treeNode(1)
    return root
a=create()

def pre_order(root,s):
    if not root:
        return
    print(root.value,s)
    pre_order(root.left,'l')
    pre_order(root.right,'r')
pre_order(a,'R')


def LCA(root,n1,n2):
    if not root:
        return None
    if root.value==n1 or root.value==n2:
        return root
    left_lca=LCA(root.left,n1,n2)
    right_lca=LCA(root.right,n1,n2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca
print(LCA(a,5,4).value)