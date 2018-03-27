import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node

class Tree:
    def getEmptyBST(self):
        return None

    def getSingleNodeBST(self):
        return Node(50)

    def getValidBST(self):
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
        return node50

    def getInvalidBST(self):
        node10 = Node(10)
        node20 = Node(20)
        node50 = Node(50)
        node70 = Node(70)
        node100 = Node(100)
        node50.addLeft(node20)
        node50.addRight(node100)
        node20.addLeft(node10)
        node20.addRight(node70)
        return node50

# Solution
def isBST(node):
    if node is None:
        return False

    max = sys.maxint
    min = -sys.maxint - 1
    return preorderTraversal(node, max, min)

def preorderTraversal(node, max, min):
    if node is None:
        return True

    if node.value >= max or node.value <= min:
        return False

    return preorderTraversal(node.left, node.value, min) and preorderTraversal(node.right, max, node.value)

# Create Test Cases
tree = Tree()
root0 = tree.getEmptyBST()
root1 = tree.getValidBST()
root2 = tree.getSingleNodeBST()
root3 = tree.getInvalidBST()

testCase1 = isBST(root0)
testCase2 = isBST(root1)
testCase3 = isBST(root2)
testCase4 = isBST(root3)

# Print Results
print 'Test Cases:'
print 'Empty BST -------- Expected: False, Result:', testCase1, '>>> TEST', 'PASSED' if not testCase1 else 'FAILED'
print 'Valid BST -------- Expected: True, Result:', testCase2,'>>>>> TEST', 'PASSED' if testCase2 else 'FAILED'
print 'Single Node BST -- Expected: True, Result:', testCase3, '>>>>> TEST', 'PASSED' if testCase3 else 'FAILED'
print 'Invalid BST ------ Expected: False, Result:', testCase4, '>>> TEST', 'PASSED' if not testCase4 else 'FAILED'

# Run Python in Terminal
# $ python isBST
# Empty BST -------- Expected: False, Result: False >>> TEST PASSED
# Valid BST -------- Expected: True, Result: True >>> TEST PASSED
# Single Node BST -- Expected: True, Result: True >>> TEST PASSED
# Invalid BST ------ Expected: False, Result: True >>> TEST PASSED