
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root,1]]
        max_dep = 0
        while stack:
            root,d =stack.pop()
            if root:
                max_dep = max(max_dep,d)
                stack.append([root.left,d +1])
                stack.append([root.right,d +1])

        return max_dep

