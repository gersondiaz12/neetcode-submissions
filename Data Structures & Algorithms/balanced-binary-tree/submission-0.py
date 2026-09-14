# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def dfs(curr):
            if not curr:
                return 0
            
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            if abs(leftHeight - rightHeight) > 1:
                self.isBalanced = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.isBalanced
        