# Technical Interview Questions And Answers

### Advice
Write out the solution on a piece of paper, look at the answer only if you are stuck.

### Steps
1. Ask questions to define the scope - look out for edge cases such as validity or size of inputs
2. Give a native solution - heck the time and space complexity, test your code
3. Give a better solution - cannot heck the time and space complexity, test your code
4. Optimise the solution if possible

### Directory
- [Tree](./Tree)
  - Check if a given binary tree is valid binary search tree.
    - BST Property:
      1. left child < parent < right child
      2. Contains no duplicated value
    - Question:
      1. Each node contains integer only? Assume yes
    - Solution:
      - [using preorder traversal with maximum and minimum values [python]](./Tree/check_binary_search_tree_using_preorder)
      - [using inorder traversal and global variable [python]](./Tree/check_binary_search_tree_using_preorder)