class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# travesal post order
# left > right > root
def post(root):
    if root.left != None:
        post(root.left)
    if root.right != None:
        post(root.right)
    print(root.data)

# root > left > right
def pre(root):
    print(root.data)
    if root.left != None:
        pre(root.left)
    if root.right != None:
        pre(root.right)
    
# left > root > right
def inorder(root):
    if root.left != None:
        inorder(root.left)
    print(root.data)
    if root.right != None:
        inorder(root.right)


tree1 = tree(11)
#adding a left child
tree1.left = tree(9)
tree1.left.left = tree(7)
tree1.left.right = tree(10)
tree1.right = tree(13)
tree1.right.left = tree(12)
tree1.right.right = tree(15)
#7 > 10 > 9 > 12 > 13 > 15 > 11
post(tree1)
#11 > 9 > 7 > 10 > 15 > 12 > 13
pre(tree1)
# 7 > 9 > 10 > 11 > 12 > 13 > 15
inorder(tree1)