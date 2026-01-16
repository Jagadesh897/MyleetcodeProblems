from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def ischeck(root):
            if not root:
                return 0 
            left = ischeck(root.left)
            right = ischeck(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left,right)
        return ischeck(root) != -1

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Balanced tree [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(f"Test 1 - Balanced tree [3,9,20,null,null,15,7]: {sol.isBalanced(root1)}")  # Expected: True
    
    # Test Case 2: Unbalanced tree [1,2,2,3,3,null,null,4,4]
    #          1
    #         / \
    #        2   2
    #       / \
    #      3   3
    #     / \
    #    4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(f"Test 2 - Unbalanced tree [1,2,2,3,3,null,null,4,4]: {sol.isBalanced(root2)}")  # Expected: False
    
    # Test Case 3: Empty tree
    root3 = None
    print(f"Test 3 - Empty tree []: {sol.isBalanced(root3)}")  # Expected: True
    
    # Test Case 4: Single node tree [1]
    root4 = TreeNode(1)
    print(f"Test 4 - Single node [1]: {sol.isBalanced(root4)}")  # Expected: True
    
    # Test Case 5: Left-skewed unbalanced tree [1,2,null,3]
    #     1
    #    /
    #   2
    #  /
    # 3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    print(f"Test 5 - Left-skewed tree [1,2,null,3]: {sol.isBalanced(root5)}")  # Expected: False
    
    # Test Case 6: Balanced tree with two levels [1,2,3]
    #     1
    #    / \
    #   2   3
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    print(f"Test 6 - Balanced two-level tree [1,2,3]: {sol.isBalanced(root6)}")  # Expected: True
    
    # Test Case 7: Right-heavy but balanced [1,null,2,null,3]
    #   1
    #    \
    #     2
    #      \
    #       3
    root7 = TreeNode(1)
    root7.right = TreeNode(2)
    root7.right.right = TreeNode(3)
    print(f"Test 7 - Right-skewed tree [1,null,2,null,3]: {sol.isBalanced(root7)}")  # Expected: False
    
    # Test Case 8: Larger balanced tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   6
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    root8.right.right = TreeNode(6)
    print(f"Test 8 - Larger balanced tree: {sol.isBalanced(root8)}")  # Expected: True