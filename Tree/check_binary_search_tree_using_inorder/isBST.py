import sys
prevMin = -sys.maxint - 1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node

def isBST(node):
    if node is None:
        return False

    return inorderTraversal(node)

def inorderTraversal(node):
    if node is None:
        return True

    inorderTraversal(node.left)

    global prevMin

    if node.value <= prevMin:
        return False

    prevMin = node.value

    inorderTraversal(node.right)

    return True


node5 = Node(5)
node10 = Node(10)
node20 = Node(20)
node25 = Node(25)
node30 = Node(30)
node50 = Node(50)
node70 = Node(70)
node75 = Node(75)
node80 = Node(80)
node100 = Node(100)
node150 = Node(150)

# BST
node50.addLeft(node10)
node50.addRight(node100)
node10.addLeft(node5)
node10.addRight(node20)
node20.addRight(node30)
node30.addLeft(node25)
node100.addLeft(node70)
node100.addRight(node150)
node70.addRight(node80)
node80.addLeft(node75)

# NOT BST
# node50.addLeft(node20)
# node50.addRight(node100)
# node20.addLeft(node10)
# node20.addRight(node70)


print isBST(node50)