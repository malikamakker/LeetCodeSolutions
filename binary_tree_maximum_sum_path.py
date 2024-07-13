# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root: Optional[TreeNode]):
        left_c, right_c, left_a, right_a = float('-inf'), float('-inf'), float('-inf'), float('-inf')
        if root.left == None and root.right == None:
            return root.val, float('-inf')
        if root.left:
            left_c, left_a = self.traverse(root.left)
        if root.right:
            right_c, right_a = self.traverse(root.right)
        
        max_c = max(root.val, root.val + left_c, root.val + right_c)
        max_a = max(left_a, right_a, left_c, right_c, root.val + left_c + right_c)
        if max_c > max_a:
            return max_c, float('-inf')
        else:
            return max_c, max_a

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        c, a = self.traverse(root)
        return max(c,a)
