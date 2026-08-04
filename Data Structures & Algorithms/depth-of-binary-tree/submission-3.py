# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count
        elif root.left and not root.right:
            count += 1
            count += self.maxDepth(root.left)
        elif not root.left and root.right:
            count += 1
            count += self.maxDepth(root.right)
        else:
            count += 1
            count += max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return count