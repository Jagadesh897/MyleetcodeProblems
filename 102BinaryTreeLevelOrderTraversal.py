from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard binary tree [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    print("=" * 50)
    print("Test 1 - Standard tree [3,9,20,null,null,15,7]")
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    result1 = sol.levelOrder(root1)
    print(f"Level Order: {result1}")  # Expected: [[3], [9, 20], [15, 7]]
    
    # Test Case 2: Single node [1]
    print("\n" + "=" * 50)
    print("Test 2 - Single node [1]")
    root2 = TreeNode(1)
    result2 = sol.levelOrder(root2)
    print(f"Level Order: {result2}")  # Expected: [[1]]
    
    # Test Case 3: Empty tree
    print("\n" + "=" * 50)
    print("Test 3 - Empty tree []")
    root3 = None
    result3 = sol.levelOrder(root3)
    print(f"Level Order: {result3}")  # Expected: []
    
    # Test Case 4: Left-skewed tree
    #     1
    #    /
    #   2
    #  /
    # 3
    print("\n" + "=" * 50)
    print("Test 4 - Left-skewed tree [1,2,null,3]")
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    result4 = sol.levelOrder(root4)
    print(f"Level Order: {result4}")  # Expected: [[1], [2], [3]]
    
    # Test Case 5: Right-skewed tree
    # 1
    #  \
    #   2
    #    \
    #     3
    print("\n" + "=" * 50)
    print("Test 5 - Right-skewed tree [1,null,2,null,3]")
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    result5 = sol.levelOrder(root5)
    print(f"Level Order: {result5}")  # Expected: [[1], [2], [3]]
    
    # Test Case 6: Complete binary tree
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    print("\n" + "=" * 50)
    print("Test 6 - Complete binary tree")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    result6 = sol.levelOrder(root6)
    print(f"Level Order: {result6}")  # Expected: [[1], [2, 3], [4, 5, 6, 7]]
    
    # Test Case 7: Tree with two nodes (left child only)
    #   1
    #  /
    # 2
    print("\n" + "=" * 50)
    print("Test 7 - Two nodes (left child only)")
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    result7 = sol.levelOrder(root7)
    print(f"Level Order: {result7}")  # Expected: [[1], [2]]
    
    # Test Case 8: Tree with two nodes (right child only)
    # 1
    #  \
    #   2
    print("\n" + "=" * 50)
    print("Test 8 - Two nodes (right child only)")
    root8 = TreeNode(1)
    root8.right = TreeNode(2)
    result8 = sol.levelOrder(root8)
    print(f"Level Order: {result8}")  # Expected: [[1], [2]]
    
    # Test Case 9: Larger unbalanced tree
    #          1
    #         / \
    #        2   3
    #       /     \
    #      4       5
    #     /         \
    #    6           7
    print("\n" + "=" * 50)
    print("Test 9 - Larger unbalanced tree")
    root9 = TreeNode(1)
    root9.left = TreeNode(2)
    root9.right = TreeNode(3)
    root9.left.left = TreeNode(4)
    root9.right.right = TreeNode(5)
    root9.left.left.left = TreeNode(6)
    root9.right.right.right = TreeNode(7)
    result9 = sol.levelOrder(root9)
    print(f"Level Order: {result9}")  # Expected: [[1], [2, 3], [4, 5], [6, 7]]
    
    # Test Case 10: Tree with negative values
    #       -10
    #       /  \
    #     -5    5
    #     / \
    #   -3   0
    print("\n" + "=" * 50)
    print("Test 10 - Tree with negative values")
    root10 = TreeNode(-10)
    root10.left = TreeNode(-5)
    root10.right = TreeNode(5)
    root10.left.left = TreeNode(-3)
    root10.left.right = TreeNode(0)
    result10 = sol.levelOrder(root10)
    print(f"Level Order: {result10}")  # Expected: [[-10], [-5, 5], [-3, 0]]
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")