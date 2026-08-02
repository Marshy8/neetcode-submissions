# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        leftT = self.invertTree(root.left)
        rightT = self.invertTree(root.right)

        root.right = leftT
        root.left = rightT

        return root
