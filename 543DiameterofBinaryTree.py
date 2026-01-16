from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dia(node):
            nonlocal diameter
            if not node:
                return 0
            left = dia(node.left)
            right = dia(node.right)
            
            diameter = max(diameter, left + right)
            return 1 + max(left, right)
                
        dia(root)
        return diameter


# ============================================================
# HELPER FUNCTION TO BUILD TREE FROM LIST
# ============================================================
def build_tree(values):
    """Build a binary tree from level-order list representation (None for null nodes)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# ============================================================
# TEST CASES WITH INPUTS
# ============================================================
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 60)
    print("Testing Diameter of Binary Tree Solution")
    print("=" * 60)
    print()
    
    # Test Case 1: Example from LeetCode
    # Tree:     1
    #          / \
    #         2   3
    #        / \
    #       4   5
    # Diameter: 3 (path: 4->2->1->3 or 5->2->1->3)
    print("Test Case 1: Balanced tree with diameter through root")
    tree1 = build_tree([1, 2, 3, 4, 5])
    result1 = solution.diameterOfBinaryTree(tree1)
    print(f"Input: [1, 2, 3, 4, 5]")
    print(f"Expected: 3")
    print(f"Got: {result1}")
    print(f"Status: {'PASS' if result1 == 3 else 'FAIL'}\n")
    
    # Test Case 2: Single node
    print("Test Case 2: Single node")
    tree2 = build_tree([1])
    result2 = solution.diameterOfBinaryTree(tree2)
    print(f"Input: [1]")
    print(f"Expected: 0")
    print(f"Got: {result2}")
    print(f"Status: {'PASS' if result2 == 0 else 'FAIL'}\n")
    
    # Test Case 3: Two nodes
    print("Test Case 3: Two nodes")
    tree3 = build_tree([1, 2])
    result3 = solution.diameterOfBinaryTree(tree3)
    print(f"Input: [1, 2]")
    print(f"Expected: 1")
    print(f"Got: {result3}")
    print(f"Status: {'PASS' if result3 == 1 else 'FAIL'}\n")
    
    # Test Case 4: Skewed tree (left)
    # Tree:     1
    #          /
    #         2
    #        /
    #       3
    #      /
    #     4
    # Diameter: 3 (path: 4->3->2->1)
    print("Test Case 4: Left-skewed tree")
    tree4 = build_tree([1, 2, None, 3, None, 4])
    result4 = solution.diameterOfBinaryTree(tree4)
    print(f"Input: [1, 2, None, 3, None, 4]")
    print(f"Expected: 3")
    print(f"Got: {result4}")
    print(f"Status: {'PASS' if result4 == 3 else 'FAIL'}\n")
    
    # Test Case 5: Diameter doesn't pass through root
    # Tree:       1
    #            /
    #           2
    #          / \
    #         3   4
    #        / \
    #       5   6
    # Diameter: 4 (path: 5->3->2->4 or 6->3->2->4)
    print("Test Case 5: Diameter doesn't pass through root")
    tree5 = build_tree([1, 2, None, 3, 4, 5, 6])
    result5 = solution.diameterOfBinaryTree(tree5)
    print(f"Input: [1, 2, None, 3, 4, 5, 6]")
    print(f"Expected: 4")
    print(f"Got: {result5}")
    print(f"Status: {'PASS' if result5 == 4 else 'FAIL'}\n")
    
    # Test Case 6: Complete binary tree
    # Tree:       1
    #           /   \
    #          2     3
    #         / \   / \
    #        4   5 6   7
    # Diameter: 4 (multiple paths possible)
    print("Test Case 6: Complete binary tree")
    tree6 = build_tree([1, 2, 3, 4, 5, 6, 7])
    result6 = solution.diameterOfBinaryTree(tree6)
    print(f"Input: [1, 2, 3, 4, 5, 6, 7]")
    print(f"Expected: 4")
    print(f"Got: {result6}")
    print(f"Status: {'PASS' if result6 == 4 else 'FAIL'}\n")
    
    # Test Case 7: Unbalanced tree
    # Tree:         1
    #              / \
    #             2   3
    #            /
    #           4
    #          /
    #         5
    # Diameter: 4 (path: 5->4->2->1->3)
    print("Test Case 7: Unbalanced tree")
    tree7 = build_tree([1, 2, 3, 4, None, None, None, 5])
    result7 = solution.diameterOfBinaryTree(tree7)
    print(f"Input: [1, 2, 3, 4, None, None, None, 5]")
    print(f"Expected: 4")
    print(f"Got: {result7}")
    print(f"Status: {'PASS' if result7 == 4 else 'FAIL'}\n")
    
    # Test Case 8: Right-skewed tree
    print("Test Case 8: Right-skewed tree")
    tree8 = build_tree([1, None, 2, None, 3, None, 4])
    result8 = solution.diameterOfBinaryTree(tree8)
    print(f"Input: [1, None, 2, None, 3, None, 4]")
    print(f"Expected: 3")
    print(f"Got: {result8}")
    print(f"Status: {'PASS' if result8 == 3 else 'FAIL'}\n")
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)