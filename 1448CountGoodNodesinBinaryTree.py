# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return root
        

        def good(node,val):
            if not node:
                return 0
            count = 1 if node.val >= val else  0
            val = max(val,node.val)
            left = good(node.left,val)
            right = good(node.right,val)
            return left + right + count

        return good(root,-100000)