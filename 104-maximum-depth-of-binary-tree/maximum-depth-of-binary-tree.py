# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if not node.right and not node.left:
                return 1
            left_depth = dfs(node.left)+1
            right_depth = dfs(node.right)+1
            return  max(left_depth,right_depth)
        return dfs(root)
