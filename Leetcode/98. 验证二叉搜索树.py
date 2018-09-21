# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            self.tempVa
            self.isValidBST_Helper(root)
        else:
            return True

    def isValidBST_Helper(self, node, Val):
        if node:
            Val = node.val
            if node.left:
                self.isValidBST_Helper(node.left, Val)
                if node.left.val >= node.val or (not Val and node.left.val >= Val):
                    self.flag = False
            if node.right:
                self.isValidBST_Helper(node.right, Val)
                if node.right.val <= node.val or (not Val and node.left.val >= Val):
                    self.flag = False
