# Technical Interview Questions And Answers

### Advice
Write out the solution on a piece of paper, look at the answer only if you are stuck.

### Steps
1. Ask questions to define the scope - look out for edge cases such as validity or size of inputs
2. Give a naive solution - heck the time and space complexity, test your code
3. Give a better solution - cannot heck the time and space complexity, test your code
4. Optimise the solution if possible

### Directory
- [Tree](./Tree)
  - Check if a given binary tree is a valid binary search tree.
    - BST Property:
      1. left child < parent < right child
      2. Contains no duplicate value
    - Ask Question:
      1. Do we allow duplicate value? Nope, if we do, then just remove = sign when we are checking for prevMin, or min max values.
    - Solution:
      - Naive:
        - [using inorder traversal and global variable [Recursive] [Python]](./Tree/check_for_valid_binary_search_tree/using_inorder_recursive)
          - Time Complexity: O(n) where n is the number of nodes in a tree
          - Space Complexity: O(n) due to recursion call stack, O(1) because global variable size will not increase with respect to input size
          - But global variable is ugly
        - [using inorder traversal and global variable [Iterative] [Python]](./Tree/check_for_valid_binary_search_tree/using_inorder_iterative)
          - Time Complexity: O(n) for the two while loops
            - while stack or currentNode: -> O(n) where n is the number of nodes pop from stack
            - while cur: -> O(k) where k is the number of left nodes, worst case O(n)
            - both while loops add up to O(n + n) = O(2n) = O(n)
          - Space Complexity: O(n) due to additional stack
      - Better:
        - [using preorder traversal with maximum and minimum values [Python]](./Tree/check_for_valid_binary_search_tree/using_preorder_recursive)
          - Global variable is so ugly so this is better
          - Time Complexity: O(n) where n is the number of nodes in a tree
          - Space Complexity: O(n) due to recursion call stack, O(1) because we don't need to store any value
      - Even better:
        - Traverse without stack or recursion is possibruuuu, let me study harder
          - Time Complexity: O(n)
          - Space Complexity: O(1)

- [Array](./Array)
  - Get median of 2 sorted arrays
  - Median property:
    - Middle number
    - Given an odd number array: [1, 2, 3], median is 2
    - Given an even number array: [1, 2, 3, 4], median is averge of 2 + 3
  - Ask Question:
    - Nah.
  - Solution:
      - Naive:
        - [merge 2 sorted arrays, sort again, then get the middle value [Python]](./Array/getMedianOf2SortedArrays)
        - Time Complexity: O(klogk) where k is the total length of two arrays
        - Space Complexity: O(k)
### Programming Language
- [Python](./Python)
  - [Recursion](./Python/recursion.py)


### Contribute
Solutions may be awfully wrong so I need your help to point them out. You can either do a PR or create an issue or give me a tight slap.