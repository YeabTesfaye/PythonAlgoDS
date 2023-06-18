# Binary Search Tree

A Binary Search Tree (BST) is a binary tree data structure that follows the property that for each node, all the values in its left subtree are less than the node's value, and all the values in its right subtree are greater than the node's value. This property enables efficient searching, insertion, and deletion operations.

## Time and Space Complexity (Average Case)

| Method                 | Description                                      | Time Complexity  | Space Complexity |
|------------------------|--------------------------------------------------|------------------|------------------|
| Insertion              | Inserts a value into the BST                     | O(log n)         | O(log n)         |
| Deletion               | Deletes a value from the BST                     | O(log n)         | O(log n)         |
| Search                 | Searches for a value in the BST                  | O(log n)         | O(log n)         |
| Update                 | Updates the value of a node in the BST           | O(log n)         | O(log n)         |
| Inorder Traversal      | Visits each node in ascending order              | O(n)             | O(n)             |
| Preorder Traversal     | Visits each node in pre-order traversal          | O(n)             | O(n)             |
| Postorder Traversal    | Visits each node in post-order traversal         | O(n)             | O(n)             |

## Balanced Tree

A balanced tree refers to a tree in which the heights of its left and right subtrees are roughly equal or differ by at most a constant factor. 

Balanced trees are important because they provide efficient search, insertion, and deletion operations. When a tree is balanced, the height of the tree is logarithmic in the number of nodes, resulting in faster operations compared to unbalanced trees.