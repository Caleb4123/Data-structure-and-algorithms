class tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# travesal post order
def post(root):
    if root.left != None:
        post(root.left)
    if root.right != None:
        post(root.right)
    print(root.data)

tree1 = tree(11)
#adding a left child
tree1.left = tree(9)
tree1.left.left = tree(7)
tree1.left.right = tree(10)
tree1.right = tree(15)
tree1.right.left = tree(12)
tree1.right.right = tree(13)
#7 > 10 > 9 > 12 > 13 > 15 > 11
post(tree1)