class tree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root.left != None:
        inorder(root.left)
    print(root.data)
    if root.right != None:
        inorder(root.right)
#function for inserting a new value

def insert(root,value):
    if root == None:
        return tree(value)
    if value > root.data:
        root.right = insert(root.right,value)
    else:
        root.left = insert(root.left,value)
    return root

def search(root,item):
    if root.data == item:
        return root
    elif root.data > item and root.left != None:
        return search(root.left,item)
    elif root.data < item and root.right != None:
        return search(root.right,item)
    else:
        return -1

#number of items
num = int(input("How many items are in the tree? "))
root = None
for i in range(num):
    node = int(input("What value should be used: "))
    root = insert(root,node)
inorder(root)

searched = int(input("Enter the item to be searched for: "))
value2 = search(root,searched)
if value2 == -1:
    print("The item is not in the tree")
else:
    print("The item is present in the tree")





