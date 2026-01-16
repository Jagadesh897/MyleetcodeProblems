from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if (root.val == subRoot.val) and self.ischeck(root,subRoot):
            return True

        else:
            
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def ischeck(self,root,subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or (root.val != subRoot.val):
            return False
        return self.ischeck(root.left,subRoot.left) and self.ischeck(root.right,subRoot.right)

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Valid subtree - subRoot is in the left subtree
    # Root:        3              SubRoot:  4
    #             / \                      / \
    #            4   5                    1   2
    #           / \
    #          1   2
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    
    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)
    print(f"Test 1 - Valid subtree in left: {sol.isSubtree(root1, subRoot1)}")  # Expected: True
    
    # Test Case 2: Not a subtree - values match but structure doesn't
    # Root:        3              SubRoot:  4
    #             / \                      / \
    #            4   5                    1   2
    #           / \
    #          1   2
    #             /
    #            0
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)
    
    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)
    print(f"Test 2 - Not a subtree (extra node): {sol.isSubtree(root2, subRoot2)}")  # Expected: False
    
    # Test Case 3: SubRoot is a single node in the tree
    # Root:        3              SubRoot:  5
    #             / \
    #            4   5
    root3 = TreeNode(3)
    root3.left = TreeNode(4)
    root3.right = TreeNode(5)
    
    subRoot3 = TreeNode(5)
    print(f"Test 3 - Single node subtree: {sol.isSubtree(root3, subRoot3)}")  # Expected: True
    
    # Test Case 4: SubRoot equals root (entire tree is subtree)
    # Root:        1              SubRoot:  1
    #             / \                      / \
    #            2   3                    2   3
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    
    subRoot4 = TreeNode(1)
    subRoot4.left = TreeNode(2)
    subRoot4.right = TreeNode(3)
    print(f"Test 4 - Entire tree is subtree: {sol.isSubtree(root4, subRoot4)}")  # Expected: True
    
    # Test Case 5: SubRoot not in tree (value doesn't exist)
    # Root:        1              SubRoot:  5
    #             / \
    #            2   3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    
    subRoot5 = TreeNode(5)
    print(f"Test 5 - SubRoot not in tree: {sol.isSubtree(root5, subRoot5)}")  # Expected: False
    
    # Test Case 6: Root is single node, SubRoot is single node (match)
    # Root:  1                   SubRoot:  1
    root6 = TreeNode(1)
    subRoot6 = TreeNode(1)
    print(f"Test 6 - Both single nodes (match): {sol.isSubtree(root6, subRoot6)}")  # Expected: True
    
    # Test Case 7: Root is single node, SubRoot is single node (no match)
    # Root:  1                   SubRoot:  2
    root7 = TreeNode(1)
    subRoot7 = TreeNode(2)
    print(f"Test 7 - Both single nodes (no match): {sol.isSubtree(root7, subRoot7)}")  # Expected: False
    
    # Test Case 8: SubRoot in right subtree
    # Root:        10             SubRoot:  5
    #             /  \                     / \
    #            4    5                   1   2
    #                / \
    #               1   2
    root8 = TreeNode(10)
    root8.left = TreeNode(4)
    root8.right = TreeNode(5)
    root8.right.left = TreeNode(1)
    root8.right.right = TreeNode(2)
    
    subRoot8 = TreeNode(5)
    subRoot8.left = TreeNode(1)
    subRoot8.right = TreeNode(2)
    print(f"Test 8 - Valid subtree in right: {sol.isSubtree(root8, subRoot8)}")  # Expected: True
    
    # Test Case 9: Same values but different structure
    # Root:        1              SubRoot:  1
    #             /                        /
    #            1                        1
    #           /                          \
    #          1                            1
    root9 = TreeNode(1)
    root9.left = TreeNode(1)
    root9.left.left = TreeNode(1)
    
    subRoot9 = TreeNode(1)
    subRoot9.left = TreeNode(1)
    subRoot9.left.right = TreeNode(1)
    print(f"Test 9 - Same values, different structure: {sol.isSubtree(root9, subRoot9)}")  # Expected: False
    
    # Test Case 10: Larger tree with subtree deep inside
    # Root:           1           SubRoot:  6
    #               /   \                  / \
    #              2     3                7   8
    #             / \   / \
    #            4   5 6   9
    #                 / \
    #                7   8
    root10 = TreeNode(1)
    root10.left = TreeNode(2)
    root10.right = TreeNode(3)
    root10.left.left = TreeNode(4)
    root10.left.right = TreeNode(5)
    root10.right.left = TreeNode(6)
    root10.right.right = TreeNode(9)
    root10.right.left.left = TreeNode(7)
    root10.right.left.right = TreeNode(8)
    
    subRoot10 = TreeNode(6)
    subRoot10.left = TreeNode(7)
    subRoot10.right = TreeNode(8)
    print(f"Test 10 - Subtree deep in tree: {sol.isSubtree(root10, subRoot10)}")  # Expected: True