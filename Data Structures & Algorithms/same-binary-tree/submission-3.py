# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        pt = []
        qt = []

        def listTravP(node):
            if node:
                pt.append(node.val) 
                listTravP(node.left)  
                listTravP(node.right)
            else:
                pt.append(None)
        def listTravQ(node):
            if node:
                qt.append(node.val)
                listTravQ(node.left) 
                listTravQ(node.right)
            else:
                qt.append(None)

        listTravP(p)
        listTravQ(q)

        print(list(pt))
        print(list(qt))

        return pt == qt
