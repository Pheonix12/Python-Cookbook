class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self, root):
        self.root = root

    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal.append(start.value)
            traversal = self.in_order(start.right, traversal)
        return traversal


def arr_to_tree(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = arr_to_tree(arr, root.left, 2*i+1, n)
        root.right = arr_to_tree(arr, root.left, 2*i+2, n)
    return root
    
def lca(root, n1, n2):
     
    # Base Case
    if root is None:
        return None

    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)

    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root


li = []

root = None
root = arr_to_tree(li, root, 0, len(li))
bst = BST(root)
print(bst.in_order(root, []))

t = lca(root, n1, n2)

 
