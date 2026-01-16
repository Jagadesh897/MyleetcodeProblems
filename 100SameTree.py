from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q or not p or (p.val != q.val):
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Identical trees [1,2,3]
    #     1           1
    #    / \         / \
    #   2   3       2   3
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    print(f"Test 1 - Identical trees [1,2,3]: {sol.isSameTree(p1, q1)}")  # Expected: True
    
    # Test Case 2: Different structure [1,2] vs [1,null,2]
    #     1           1
    #    /             \
    #   2               2
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    print(f"Test 2 - Different structure [1,2] vs [1,null,2]: {sol.isSameTree(p2, q2)}")  # Expected: False
    
    # Test Case 3: Different values [1,2,1] vs [1,1,2]
    #     1           1
    #    / \         / \
    #   2   1       1   2
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    
    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)
    print(f"Test 3 - Different values [1,2,1] vs [1,1,2]: {sol.isSameTree(p3, q3)}")  # Expected: False
    
    # Test Case 4: Both empty trees
    p4 = None
    q4 = None
    print(f"Test 4 - Both empty trees []: {sol.isSameTree(p4, q4)}")  # Expected: True
    
    # Test Case 5: One empty, one not [1] vs []
    p5 = TreeNode(1)
    q5 = None
    print(f"Test 5 - One empty [1] vs []: {sol.isSameTree(p5, q5)}")  # Expected: False
    
    # Test Case 6: Single node identical [1] vs [1]
    p6 = TreeNode(1)
    q6 = TreeNode(1)
    print(f"Test 6 - Single node identical [1]: {sol.isSameTree(p6, q6)}")  # Expected: True
    
    # Test Case 7: Single node different [1] vs [2]
    p7 = TreeNode(1)
    q7 = TreeNode(2)
    print(f"Test 7 - Single node different [1] vs [2]: {sol.isSameTree(p7, q7)}")  # Expected: False
    
    # Test Case 8: Larger identical trees
    #        1               1
    #       / \             / \
    #      2   3           2   3
    #     / \   \         / \   \
    #    4   5   6       4   5   6
    p8 = TreeNode(1)
    p8.left = TreeNode(2)
    p8.right = TreeNode(3)
    p8.left.left = TreeNode(4)
    p8.left.right = TreeNode(5)
    p8.right.right = TreeNode(6)
    
    q8 = TreeNode(1)
    q8.left = TreeNode(2)
    q8.right = TreeNode(3)
    q8.left.left = TreeNode(4)
    q8.left.right = TreeNode(5)
    q8.right.right = TreeNode(6)
    print(f"Test 8 - Larger identical trees: {sol.isSameTree(p8, q8)}")  # Expected: True
    
    # Test Case 9: Larger trees with one difference
    #        1               1
    #       / \             / \
    #      2   3           2   3
    #     / \   \         / \   \
    #    4   5   6       4   7   6  (5 vs 7)
    p9 = TreeNode(1)
    p9.left = TreeNode(2)
    p9.right = TreeNode(3)
    p9.left.left = TreeNode(4)
    p9.left.right = TreeNode(5)
    p9.right.right = TreeNode(6)
    
    q9 = TreeNode(1)
    q9.left = TreeNode(2)
    q9.right = TreeNode(3)
    q9.left.left = TreeNode(4)
    q9.left.right = TreeNode(7)
    q9.right.right = TreeNode(6)
    print(f"Test 9 - Larger trees with one difference: {sol.isSameTree(p9, q9)}")  # Expected: False
    
    # Test Case 10: Mirror trees (different structure)
    #     1           1
    #    /             \
    #   2               2
    #  /                 \
    # 3                   3
    p10 = TreeNode(1)
    p10.left = TreeNode(2)
    p10.left.left = TreeNode(3)
    
    q10 = TreeNode(1)
    q10.right = TreeNode(2)
    q10.right.right = TreeNode(3)
    print(f"Test 10 - Mirror trees: {sol.isSameTree(p10, q10)}")  # Expected: False