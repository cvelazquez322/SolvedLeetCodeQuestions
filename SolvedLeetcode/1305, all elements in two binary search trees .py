
# Given two binary search trees root1 and root2.

# Return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preHelper(root, returned_list):
    if root is None:
        return []
    returned_list.append(root.val)
    if root.left:
        preHelper(root.left, returned_list)
        
    if root.right:
        preHelper(root.right, returned_list)

    return returned_list

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        r1list = preHelper(root1, [])
        r2list = preHelper(root2, [])
        r1list = r1list + r2list
        r1list.sort()
        return r1list
        