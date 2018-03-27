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

    def getDuplicatedBST(self):
        node50 = Node(50)
        node50left = Node(50)
        node50Right = Node(50)
        node50.addLeft(node50left)
        node50.addRight(node50Right)
        return node50

# Solution
def isBST(node):
    prevMin = -sys.maxint - 1

    if not node:
        return False

    currentNode = node
    stack = []

    while currentNode or stack:
        while currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left

        currentNode = stack.pop()
        if currentNode.value <= prevMin:
            return False
        prevMin = currentNode.value

        currentNode = currentNode.right

    return True


# Create Test Cases
tree = Tree()
root1 = tree.getEmptyBST()
root2 = tree.getValidBST()
root3 = tree.getSingleNodeBST()
root4 = tree.getInvalidBST()
root5 = tree.getDuplicatedBST()

testCase1 = isBST(root1)
testCase2 = isBST(root2)
testCase3 = isBST(root3)
testCase4 = isBST(root4)
testCase5 = isBST(root5)
# Print Results
print 'Test Cases:'
print 'Empty BST ------------------ Expected: False, Result:', testCase1, '>>> TEST', 'PASSED' if not testCase1 else 'FAILED'
print 'Valid BST ------------------ Expected: True, Result:', testCase2,'>>>>> TEST', 'PASSED' if testCase2 else 'FAILED'
print 'Single Node BST ------------ Expected: True, Result:', testCase3, '>>>>> TEST', 'PASSED' if testCase3 else 'FAILED'
print 'Invalid BST ---------------- Expected: False, Result:', testCase4, '>>> TEST', 'PASSED' if not testCase4 else 'FAILED'
print 'Duplicated values BST ------ Expected: False, Result:', testCase5, '>>> TEST', 'PASSED' if not testCase5 else 'FAILED'

# Run Python in Terminal
# $ python isBST
# Empty BST -------- Expected: False, Result: False >>> TEST PASSED
# Valid BST -------- Expected: True, Result: True >>> TEST PASSED
# Single Node BST -- Expected: True, Result: True >>> TEST PASSED
# Invalid BST ------ Expected: False, Result: True >>> TEST PASSED
# Duplicated values BST ------ Expected: False, Result: False >>> TEST PASSED
