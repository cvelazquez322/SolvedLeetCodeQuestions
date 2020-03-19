# # We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preHelper(root, returned_list):
    returned_list.append(root.val)
    if root.left:
        preHelper(root.left, returned_list)
        
    if root.right:
        preHelper(root.right, returned_list)

    return returned_list
    


def preorderTraversal(root):
    if root is None:
        return
    #ULR
    #value list
    vlist = []
    return preHelper(root, vlist)

def check0s(root):
    tmplist = []
    tmplist = preorderTraversal(root)
    for i in tmplist:
        if i != 0:
            return False
    return True

def pruneHelper(root):
    if root.left:
        if check0s(root.left):
            root.left = None
    if root.right:
        if check0s(root.right):
            root.right = None
    if root.left:
        pruneHelper(root.left)
    if root.right:
        pruneHelper(root.right)
    return root    
    
    
    
    
    
    
    
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        return pruneHelper(root)