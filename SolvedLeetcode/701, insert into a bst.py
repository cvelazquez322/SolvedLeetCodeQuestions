# Given the root node of a binary search tree (BST) 
# and a value to be inserted into the tree, insert the value into the BST. 

# Return the root node of the BST after the insertion.
 # It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, 
# as long as the tree remains a BST after insertion. You can return any of them.


# # Definition for a binary tree node.
# # class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def iibstHelper(root, val, parent):
    if root is None:
        root = TreeNode(val)
        if root.val < parent.val:
            parent.left = root
        else:
            parent.right = root
        
        
    if root.val > val:
        iibstHelper(root.left, val, root)
    if root.val < val:
        iibstHelper(root.right, val, root)

    return root

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        return iibstHelper(root, val, None)