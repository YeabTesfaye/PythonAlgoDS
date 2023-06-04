class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_value = self._find_min(node.right)
            node.value = min_value
            node.right = self._delete_recursive(node.right, min_value)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.value
     #if key exist it will update else it will insert 
     # new node in the BST   
    def update(self,key,target):
        node = self.search(key)
        if node is not None:
            node.value = target
        else:
            node = self.insert(target)   
    #check if the BST is balanced 
    def is_balanced(self,node):
        if self.root is None:
            return True
        balanced_l, height_l = is_balanced(self)
        return balanced,hight 
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


# Example usage
bst = BinarySearchTree()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)
bst.delete(13)
bst.update(70, 9)
isExist = bst.search(13)
print(bool(isExist))
# print("Inorder traversal:")
#inorder Traversal always give a sorted list 
print(bst.inorder_traversal())

# print("Preorder traversal:")
# print(bst.preorder_traversal())

# print("Postorder traversal:")
# print(bst.postorder_traversal())


# Time complexity analysis:
# - Insertion: O(log n) on average for a balanced tree, O(n) in the worst case for an unbalanced tree.
# - Deletion: O(log n) on average for a balanced tree, O(n) in the worst case for an unbalanced tree.
# - Search: O(log n) on average for a balanced tree, O(n) in the worst case for an unbalanced tree.
# - Update: O(log n) on average fro a balancd tree, O(n) in the worst case for an  unbalanced tree
# - Inorder Traversal: O(n), as it visits each node once.
# - Preorder Traversal: O(n), as it visits each node once.
# - Postorder Traversal: O(n), as it visits each node once.


#Definition for balanced tree 

'''
A balanced tree refers to a tree in which the heights of its left and right subtrees are roughly equal
or differ by at most a constant factor. In other words,the tree is structured in a way that minimizes the height and 
ensures that the nodes are evenly distributed across the tree.

Balanced trees are important because they provide efficient search,
insertion, and deletion operations. When a tree is balanced, the height of the tree is logarithmic in the
number of nodes, resulting in faster operations compared to unbalanced trees.
 '''