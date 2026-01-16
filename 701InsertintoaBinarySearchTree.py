from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root

# Helper function to perform in-order traversal (should give sorted order for BST)
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Helper function to print tree structure (simple level-order representation)
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
    
    # Test Case 1: Insert into existing BST
    # Original BST:    4
    #                 / \
    #                2   7
    #               / \
    #              1   3
    # Insert: 5
    print("=" * 50)
    print("Test 1 - Insert 5 into BST [4,2,7,1,3]")
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    
    print("Before insertion:")
    print("In-order:", inorder_traversal(root1))
    
    root1 = sol.insertIntoBST(root1, 5)
    print("After inserting 5:")
    print("In-order:", inorder_traversal(root1))
    print_tree(root1)
    
    # Test Case 2: Insert into empty tree
    print("\n" + "=" * 50)
    print("Test 2 - Insert 10 into empty BST")
    root2 = None
    root2 = sol.insertIntoBST(root2, 10)
    print("After inserting 10:")
    print("In-order:", inorder_traversal(root2))
    print_tree(root2)
    
    # Test Case 3: Insert smaller value (goes to left)
    print("\n" + "=" * 50)
    print("Test 3 - Insert 3 into BST [5]")
    root3 = TreeNode(5)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root3))
    
    root3 = sol.insertIntoBST(root3, 3)
    print("After inserting 3:")
    print("In-order:", inorder_traversal(root3))
    print_tree(root3)
    
    # Test Case 4: Insert larger value (goes to right)
    print("\n" + "=" * 50)
    print("Test 4 - Insert 7 into BST [5,3]")
    root4 = TreeNode(5)
    root4.left = TreeNode(3)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root4))
    
    root4 = sol.insertIntoBST(root4, 7)
    print("After inserting 7:")
    print("In-order:", inorder_traversal(root4))
    print_tree(root4)
    
    # Test Case 5: Multiple insertions to build a BST
    print("\n" + "=" * 50)
    print("Test 5 - Build BST by inserting [5, 3, 7, 1, 9, 4, 6]")
    root5 = None
    values = [5, 3, 7, 1, 9, 4, 6]
    for val in values:
        root5 = sol.insertIntoBST(root5, val)
        print(f"After inserting {val}: {inorder_traversal(root5)}")
    print("\nFinal tree structure:")
    print_tree(root5)
    
    # Test Case 6: Insert into left-skewed tree
    print("\n" + "=" * 50)
    print("Test 6 - Insert 2 into left-skewed BST [5,3,1]")
    root6 = TreeNode(5)
    root6.left = TreeNode(3)
    root6.left.left = TreeNode(1)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root6))
    
    root6 = sol.insertIntoBST(root6, 2)
    print("After inserting 2:")
    print("In-order:", inorder_traversal(root6))
    print_tree(root6)
    
    # Test Case 7: Insert into right-skewed tree
    print("\n" + "=" * 50)
    print("Test 7 - Insert 4 into right-skewed BST [1,3,5]")
    root7 = TreeNode(1)
    root7.right = TreeNode(3)
    root7.right.right = TreeNode(5)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root7))
    
    root7 = sol.insertIntoBST(root7, 4)
    print("After inserting 4:")
    print("In-order:", inorder_traversal(root7))
    print_tree(root7)
    
    # Test Case 8: Insert maximum value
    print("\n" + "=" * 50)
    print("Test 8 - Insert 100 (max) into BST [50,25,75]")
    root8 = TreeNode(50)
    root8.left = TreeNode(25)
    root8.right = TreeNode(75)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root8))
    
    root8 = sol.insertIntoBST(root8, 100)
    print("After inserting 100:")
    print("In-order:", inorder_traversal(root8))
    print_tree(root8)
    
    # Test Case 9: Insert minimum value
    print("\n" + "=" * 50)
    print("Test 9 - Insert 1 (min) into BST [50,25,75]")
    root9 = TreeNode(50)
    root9.left = TreeNode(25)
    root9.right = TreeNode(75)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root9))
    
    root9 = sol.insertIntoBST(root9, 1)
    print("After inserting 1:")
    print("In-order:", inorder_traversal(root9))
    print_tree(root9)
    
    # Test Case 10: Insert into larger balanced BST
    print("\n" + "=" * 50)
    print("Test 10 - Insert 12 into larger BST")
    root10 = TreeNode(10)
    root10.left = TreeNode(5)
    root10.right = TreeNode(15)
    root10.left.left = TreeNode(3)
    root10.left.right = TreeNode(7)
    root10.right.left = TreeNode(13)
    root10.right.right = TreeNode(20)
    print("Before insertion:")
    print("In-order:", inorder_traversal(root10))
    
    root10 = sol.insertIntoBST(root10, 12)
    print("After inserting 12:")
    print("In-order:", inorder_traversal(root10))
    print_tree(root10)
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")