# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        return left or right

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Classic BST - LCA is root
    # BST:         6
    #            /   \
    #           2     8
    #          / \   / \
    #         0   4 7   9
    #            / \
    #           3   5
    # p=2, q=8, LCA=6
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    
    p1 = root1.left  # Node 2
    q1 = root1.right  # Node 8
    result1 = sol.lowestCommonAncestor(root1, p1, q1)
    print(f"Test 1 - LCA of 2 and 8: {result1.val}")  # Expected: 6
    
    # Test Case 2: LCA is one of the nodes (p is ancestor of q)
    # p=2, q=4, LCA=2
    p2 = root1.left  # Node 2
    q2 = root1.left.right  # Node 4
    result2 = sol.lowestCommonAncestor(root1, p2, q2)
    print(f"Test 2 - LCA of 2 and 4: {result2.val}")  # Expected: 2
    
    # Test Case 3: Both nodes in left subtree
    # p=0, q=5, LCA=2
    p3 = root1.left.left  # Node 0
    q3 = root1.left.right.right  # Node 5
    result3 = sol.lowestCommonAncestor(root1, p3, q3)
    print(f"Test 3 - LCA of 0 and 5: {result3.val}")  # Expected: 2
    
    # Test Case 4: Both nodes in right subtree
    # p=7, q=9, LCA=8
    p4 = root1.right.left  # Node 7
    q4 = root1.right.right  # Node 9
    result4 = sol.lowestCommonAncestor(root1, p4, q4)
    print(f"Test 4 - LCA of 7 and 9: {result4.val}")  # Expected: 8
    
    # Test Case 5: Nodes deeper in tree
    # p=3, q=5, LCA=4
    p5 = root1.left.right.left  # Node 3
    q5 = root1.left.right.right  # Node 5
    result5 = sol.lowestCommonAncestor(root1, p5, q5)
    print(f"Test 5 - LCA of 3 and 5: {result5.val}")  # Expected: 4
    
    # Test Case 6: Simple BST with 3 nodes
    # BST:    2
    #        / \
    #       1   3
    # p=1, q=3, LCA=2
    root6 = TreeNode(2)
    root6.left = TreeNode(1)
    root6.right = TreeNode(3)
    
    p6 = root6.left  # Node 1
    q6 = root6.right  # Node 3
    result6 = sol.lowestCommonAncestor(root6, p6, q6)
    print(f"Test 6 - LCA of 1 and 3 in simple BST: {result6.val}")  # Expected: 2
    
    # Test Case 7: Root and one child
    # p=2, q=1, LCA=2
    p7 = root6  # Node 2 (root)
    q7 = root6.left  # Node 1
    result7 = sol.lowestCommonAncestor(root6, p7, q7)
    print(f"Test 7 - LCA of 2 (root) and 1: {result7.val}")  # Expected: 2
    
    # Test Case 8: Left-skewed BST
    # BST:    5
    #        /
    #       3
    #      /
    #     1
    # p=1, q=3, LCA=3
    root8 = TreeNode(5)
    root8.left = TreeNode(3)
    root8.left.left = TreeNode(1)
    
    p8 = root8.left.left  # Node 1
    q8 = root8.left  # Node 3
    result8 = sol.lowestCommonAncestor(root8, p8, q8)
    print(f"Test 8 - LCA of 1 and 3 in left-skewed BST: {result8.val}")  # Expected: 3
    
    # Test Case 9: Right-skewed BST
    # BST:  1
    #        \
    #         3
    #          \
    #           5
    # p=1, q=5, LCA=1
    root9 = TreeNode(1)
    root9.right = TreeNode(3)
    root9.right.right = TreeNode(5)
    
    p9 = root9  # Node 1
    q9 = root9.right.right  # Node 5
    result9 = sol.lowestCommonAncestor(root9, p9, q9)
    print(f"Test 9 - LCA of 1 and 5 in right-skewed BST: {result9.val}")  # Expected: 1
    
    # Test Case 10: Larger BST
    # BST:           10
    #              /    \
    #             5      15
    #            / \    /  \
    #           3   7  12  20
    #          /   /     \
    #         1   6      13
    # p=1, q=7, LCA=5
    root10 = TreeNode(10)
    root10.left = TreeNode(5)
    root10.right = TreeNode(15)
    root10.left.left = TreeNode(3)
    root10.left.right = TreeNode(7)
    root10.right.left = TreeNode(12)
    root10.right.right = TreeNode(20)
    root10.left.left.left = TreeNode(1)
    root10.left.right.left = TreeNode(6)
    root10.right.left.right = TreeNode(13)
    
    p10 = root10.left.left.left  # Node 1
    q10 = root10.left.right  # Node 7
    result10 = sol.lowestCommonAncestor(root10, p10, q10)
    print(f"Test 10 - LCA of 1 and 7 in larger BST: {result10.val}")  # Expected: 5
    
    # Test Case 11: Cross-subtree in larger BST
    # p=6, q=13, LCA=10
    p11 = root10.left.right.left  # Node 6
    q11 = root10.right.left.right  # Node 13
    result11 = sol.lowestCommonAncestor(root10, p11, q11)
    print(f"Test 11 - LCA of 6 and 13 in larger BST: {result11.val}")  # Expected: 10