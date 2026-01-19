from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preindex = 0
        dic = {}
        for i in range(len(inorder)):
            dic[inorder[i]]  = i
        def split(i,e):
            nonlocal preindex
            if i > e:
                return None
            pindex = dic[preorder[preindex]]
            node = TreeNode(preorder[preindex])
            preindex +=1
            node.left = split(i,dic[inorder[pindex]] - 1)
            node.right = split( dic[inorder[pindex]] + 1, e)
            return node
        return split(0,len(inorder) - 1 )

# Helper function to get preorder traversal
def get_preorder(root):
    if not root:
        return []
    return [root.val] + get_preorder(root.left) + get_preorder(root.right)

# Helper function to get inorder traversal
def get_inorder(root):
    if not root:
        return []
    return get_inorder(root.left) + [root.val] + get_inorder(root.right)

# Helper function to print tree structure
def print_tree(root, level=0, prefix="Root: "):
    if root:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: LeetCode Example
    # Tree:       3
    #            / \
    #           9  20
    #             /  \
    #            15   7
    print("=" * 60)
    print("Test 1 - LeetCode Example")
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    print(f"Preorder: {preorder1}")
    print(f"Inorder:  {inorder1}")
    
    result1 = sol.buildTree(preorder1, inorder1)
    print("\nConstructed Tree:")
    print_tree(result1)
    print(f"\nVerification - Preorder: {get_preorder(result1)}")
    print(f"Verification - Inorder:  {get_inorder(result1)}")
    
    # Test Case 2: Single node
    print("\n" + "=" * 60)
    print("Test 2 - Single node")
    preorder2 = [1]
    inorder2 = [1]
    print(f"Preorder: {preorder2}")
    print(f"Inorder:  {inorder2}")
    
    result2 = sol.buildTree(preorder2, inorder2)
    print("\nConstructed Tree:")
    print_tree(result2)
    
    # Test Case 3: Left-skewed tree
    # Tree:     1
    #          /
    #         2
    #        /
    #       3
    print("\n" + "=" * 60)
    print("Test 3 - Left-skewed tree")
    preorder3 = [1, 2, 3]
    inorder3 = [3, 2, 1]
    print(f"Preorder: {preorder3}")
    print(f"Inorder:  {inorder3}")
    
    result3 = sol.buildTree(preorder3, inorder3)
    print("\nConstructed Tree:")
    print_tree(result3)
    print(f"\nVerification - Preorder: {get_preorder(result3)}")
    print(f"Verification - Inorder:  {get_inorder(result3)}")
    
    # Test Case 4: Right-skewed tree
    # Tree:  1
    #         \
    #          2
    #           \
    #            3
    print("\n" + "=" * 60)
    print("Test 4 - Right-skewed tree")
    preorder4 = [1, 2, 3]
    inorder4 = [1, 2, 3]
    print(f"Preorder: {preorder4}")
    print(f"Inorder:  {inorder4}")
    
    result4 = sol.buildTree(preorder4, inorder4)
    print("\nConstructed Tree:")
    print_tree(result4)
    print(f"\nVerification - Preorder: {get_preorder(result4)}")
    print(f"Verification - Inorder:  {get_inorder(result4)}")
    
    # Test Case 5: Complete binary tree
    # Tree:       1
    #            / \
    #           2   3
    #          / \ / \
    #         4  5 6  7
    print("\n" + "=" * 60)
    print("Test 5 - Complete binary tree")
    preorder5 = [1, 2, 4, 5, 3, 6, 7]
    inorder5 = [4, 2, 5, 1, 6, 3, 7]
    print(f"Preorder: {preorder5}")
    print(f"Inorder:  {inorder5}")
    
    result5 = sol.buildTree(preorder5, inorder5)
    print("\nConstructed Tree:")
    print_tree(result5)
    print(f"\nVerification - Preorder: {get_preorder(result5)}")
    print(f"Verification - Inorder:  {get_inorder(result5)}")
    
    # Test Case 6: Two nodes (left child only)
    # Tree:   1
    #        /
    #       2
    print("\n" + "=" * 60)
    print("Test 6 - Two nodes (left child only)")
    preorder6 = [1, 2]
    inorder6 = [2, 1]
    print(f"Preorder: {preorder6}")
    print(f"Inorder:  {inorder6}")
    
    result6 = sol.buildTree(preorder6, inorder6)
    print("\nConstructed Tree:")
    print_tree(result6)
    
    # Test Case 7: Two nodes (right child only)
    # Tree:  1
    #         \
    #          2
    print("\n" + "=" * 60)
    print("Test 7 - Two nodes (right child only)")
    preorder7 = [1, 2]
    inorder7 = [1, 2]
    print(f"Preorder: {preorder7}")
    print(f"Inorder:  {inorder7}")
    
    result7 = sol.buildTree(preorder7, inorder7)
    print("\nConstructed Tree:")
    print_tree(result7)
    
    # Test Case 8: Larger tree with negative values
    # Tree:        -10
    #             /    \
    #           -5      5
    #           / \    /
    #         -3   0  2
    print("\n" + "=" * 60)
    print("Test 8 - Tree with negative values")
    preorder8 = [-10, -5, -3, 0, 5, 2]
    inorder8 = [-3, -5, 0, -10, 2, 5]
    print(f"Preorder: {preorder8}")
    print(f"Inorder:  {inorder8}")
    
    result8 = sol.buildTree(preorder8, inorder8)
    print("\nConstructed Tree:")
    print_tree(result8)
    print(f"\nVerification - Preorder: {get_preorder(result8)}")
    print(f"Verification - Inorder:  {get_inorder(result8)}")
    
    # Test Case 9: Unbalanced tree
    # Tree:       5
    #            / \
    #           3   8
    #          /   / \
    #         1   6   9
    #          \
    #           2
    print("\n" + "=" * 60)
    print("Test 9 - Unbalanced tree")
    preorder9 = [5, 3, 1, 2, 8, 6, 9]
    inorder9 = [1, 2, 3, 5, 6, 8, 9]
    print(f"Preorder: {preorder9}")
    print(f"Inorder:  {inorder9}")
    
    result9 = sol.buildTree(preorder9, inorder9)
    print("\nConstructed Tree:")
    print_tree(result9)
    print(f"\nVerification - Preorder: {get_preorder(result9)}")
    print(f"Verification - Inorder:  {get_inorder(result9)}")
    
    # Test Case 10: Empty arrays
    print("\n" + "=" * 60)
    print("Test 10 - Empty arrays")
    preorder10 = []
    inorder10 = []
    print(f"Preorder: {preorder10}")
    print(f"Inorder:  {inorder10}")
    
    result10 = sol.buildTree(preorder10, inorder10)
    print(f"Result: {result10}")  # Expected: None
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")