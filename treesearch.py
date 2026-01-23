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
#function for minimum value node

def minimum(root):
    mini = root
    while mini.left != None:
        mini = mini.left
    return mini


def delete(root,item):
    if root is None:
        return root
    elif item < root.data:
        root.left = delete(root.left,item)
    elif item > root.data:
        root.right = delete(root.right,item)
    else:
        if root.left is None and root.right is None:
            return None
            #root has only 1 child
        elif root.left is None:
            var = root.right 
            #root = None
            return var
        elif root.right is None:
            var = root.right
            #root = None
            return var
        #if root has 2 child
        #else:
        var = minimum(root.right)
        #print(var.data)
        #temp = root.data
        root.data = var.data
        #var.data = temp
        root.right = delete(root.right,var.data)
    return root
#number of items
num = int(input("How many items are in the tree? "))
root = None
for i in range(num):
    node = int(input("What value should be used: "))
    root = insert(root,node)
inorder(root)

searched = int(input("Enter the item to be searched for: "))
print(searched,"is on level")
value2 = search(root,searched)
if value2 == -1:
    print("The item is not in the tree")
else:
    print("The item is present in the tree")

user = int(input("Enter the number to delete: "))
var2 = delete(root,user)

print("tree after deletion")
inorder(root)

