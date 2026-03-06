# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,targetSum):
            if not node:
                return False
            if not node.right and not node.left:
                return targetSum - node.val == 0
            targetSum -= node.val
            target_l=dfs(node.left,targetSum)
            target_r=dfs(node.right,targetSum)
            return target_r or target_l
        return dfs(root,targetSum)