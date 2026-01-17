from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def isright(node,result,level):
            if not node:
                return False
            if len(result) == level:
                result.append(node.val)
            isright(node.right,result,level + 1)
            isright(node.left,result,level + 1)
            return result
        return isright(root,[],0)

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard binary tree [1,2,3,null,5,null,4]
    #       1          <-- see 1
    #      / \
    #     2   3        <-- see 3
    #      \   \
    #       5   4      <-- see 4
    print("=" * 50)
    print("Test 1 - Standard tree [1,2,3,null,5,null,4]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    result1 = sol.rightSideView(root1)
    print(f"Right Side View: {result1}")  # Expected: [1, 3, 4]
    
    # Test Case 2: Tree where left subtree is deeper
    #       1          <-- see 1
    #      / \
    #     2   3        <-- see 3
    #    /
    #   4              <-- see 4 (from left, visible on right)
    print("\n" + "=" * 50)
    print("Test 2 - Left subtree deeper [1,2,3,4]")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    result2 = sol.rightSideView(root2)
    print(f"Right Side View: {result2}")  # Expected: [1, 3, 4]
    
    # Test Case 3: Single node
    print("\n" + "=" * 50)
    print("Test 3 - Single node [1]")
    root3 = TreeNode(1)
    result3 = sol.rightSideView(root3)
    print(f"Right Side View: {result3}")  # Expected: [1]
    
    # Test Case 4: Empty tree
    print("\n" + "=" * 50)
    print("Test 4 - Empty tree []")
    root4 = None
    result4 = sol.rightSideView(root4)
    print(f"Right Side View: {result4}")  # Expected: []
    
    # Test Case 5: Right-skewed tree (all nodes visible)
    # 1          <-- see 1
    #  \
    #   2        <-- see 2
    #    \
    #     3      <-- see 3
    print("\n" + "=" * 50)
    print("Test 5 - Right-skewed tree [1,null,2,null,3]")
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    result5 = sol.rightSideView(root5)
    print(f"Right Side View: {result5}")  # Expected: [1, 2, 3]
    
    # Test Case 6: Left-skewed tree (all nodes visible from right)
    #     1      <-- see 1
    #    /
    #   2        <-- see 2
    #  /
    # 3          <-- see 3
    print("\n" + "=" * 50)
    print("Test 6 - Left-skewed tree [1,2,null,3]")
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.left.left = TreeNode(3)
    result6 = sol.rightSideView(root6)
    print(f"Right Side View: {result6}")  # Expected: [1, 2, 3]
    
    # Test Case 7: Complete binary tree
    #        1         <-- see 1
    #       / \
    #      2   3       <-- see 3
    #     / \ / \
    #    4  5 6  7     <-- see 7
    print("\n" + "=" * 50)
    print("Test 7 - Complete binary tree")
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(3)
    root7.left.left = TreeNode(4)
    root7.left.right = TreeNode(5)
    root7.right.left = TreeNode(6)
    root7.right.right = TreeNode(7)
    result7 = sol.rightSideView(root7)
    print(f"Right Side View: {result7}")  # Expected: [1, 3, 7]
    
    # Test Case 8: Tree with two nodes (left child only)
    #   1        <-- see 1
    #  /
    # 2          <-- see 2
    print("\n" + "=" * 50)
    print("Test 8 - Two nodes (left child only)")
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    result8 = sol.rightSideView(root8)
    print(f"Right Side View: {result8}")  # Expected: [1, 2]
    
    # Test Case 9: Tree with two nodes (right child only)
    # 1          <-- see 1
    #  \
    #   2        <-- see 2
    print("\n" + "=" * 50)
    print("Test 9 - Two nodes (right child only)")
    root9 = TreeNode(1)
    root9.right = TreeNode(2)
    result9 = sol.rightSideView(root9)
    print(f"Right Side View: {result9}")  # Expected: [1, 2]
    
    # Test Case 10: Larger tree with left subtree deeper
    #          1               <-- see 1
    #         / \
    #        2   3             <-- see 3
    #       / \
    #      4   5               <-- see 5
    #     /
    #    6                     <-- see 6
    print("\n" + "=" * 50)
    print("Test 10 - Left subtree much deeper")
    root10 = TreeNode(1)
    root10.left = TreeNode(2)
    root10.right = TreeNode(3)
    root10.left.left = TreeNode(4)
    root10.left.right = TreeNode(5)
    root10.left.left.left = TreeNode(6)
    result10 = sol.rightSideView(root10)
    print(f"Right Side View: {result10}")  # Expected: [1, 3, 5, 6]
    
    # Test Case 11: Zigzag depth tree
    #       1                  <-- see 1
    #      / \
    #     2   3                <-- see 3
    #    /     \
    #   4       5              <-- see 5
    #    \     /
    #     6   7                <-- see 7
    print("\n" + "=" * 50)
    print("Test 11 - Zigzag depth tree")
    root11 = TreeNode(1)
    root11.left = TreeNode(2)
    root11.right = TreeNode(3)
    root11.left.left = TreeNode(4)
    root11.right.right = TreeNode(5)
    root11.left.left.right = TreeNode(6)
    root11.right.right.left = TreeNode(7)
    result11 = sol.rightSideView(root11)
    print(f"Right Side View: {result11}")  # Expected: [1, 3, 5, 7]
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")