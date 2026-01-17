from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Find the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found - handle three cases
            
            # Case 1: Node has no left child
            if not root.left:
                return root.right
            
            # Case 2: Node has no right child
            if not root.right:
                return root.left
            
            # Case 3: Node has both children
            # Find the inorder successor (smallest in right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace current node's value with successor's value
            root.val = successor.val
            
            # Delete the successor from right subtree
            root.right = self.deleteNode(root.right, successor.val)
        
        return root

# Helper function to perform in-order traversal (should give sorted order for BST)
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

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
    
    # Test Case 1: Delete node with two children (classic case)
    # BST:         5
    #            /   \
    #           3     6
    #          / \     \
    #         2   4     7
    # Delete: 3
    print("=" * 50)
    print("Test 1 - Delete node 3 (has two children)")
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(7)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root1))
    print_tree(root1)
    
    root1 = sol.deleteNode(root1, 3)
    print("\nAfter deleting 3:")
    print("In-order:", inorder_traversal(root1))
    print_tree(root1)
    
    # Test Case 2: Delete root node
    print("\n" + "=" * 50)
    print("Test 2 - Delete root node 5")
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root2))
    
    root2 = sol.deleteNode(root2, 5)
    print("After deleting root 5:")
    print("In-order:", inorder_traversal(root2))
    print_tree(root2)
    
    # Test Case 3: Delete leaf node (no children)
    print("\n" + "=" * 50)
    print("Test 3 - Delete leaf node 7")
    root3 = TreeNode(5)
    root3.left = TreeNode(3)
    root3.right = TreeNode(6)
    root3.right.right = TreeNode(7)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root3))
    
    root3 = sol.deleteNode(root3, 7)
    print("After deleting leaf 7:")
    print("In-order:", inorder_traversal(root3))
    print_tree(root3)
    
    # Test Case 4: Delete node with only left child
    print("\n" + "=" * 50)
    print("Test 4 - Delete node with only left child")
    root4 = TreeNode(5)
    root4.left = TreeNode(3)
    root4.left.left = TreeNode(2)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root4))
    
    root4 = sol.deleteNode(root4, 3)
    print("After deleting 3:")
    print("In-order:", inorder_traversal(root4))
    print_tree(root4)
    
    # Test Case 5: Delete node with only right child
    print("\n" + "=" * 50)
    print("Test 5 - Delete node with only right child")
    root5 = TreeNode(5)
    root5.right = TreeNode(7)
    root5.right.right = TreeNode(9)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root5))
    
    root5 = sol.deleteNode(root5, 7)
    print("After deleting 7:")
    print("In-order:", inorder_traversal(root5))
    print_tree(root5)
    
    # Test Case 6: Delete from single node tree
    print("\n" + "=" * 50)
    print("Test 6 - Delete from single node tree")
    root6 = TreeNode(5)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root6))
    
    root6 = sol.deleteNode(root6, 5)
    print("After deleting 5:")
    print("In-order:", inorder_traversal(root6))
    print("Tree is now empty" if not root6 else "")
    
    # Test Case 7: Key not in tree
    print("\n" + "=" * 50)
    print("Test 7 - Key not in tree (delete 10)")
    root7 = TreeNode(5)
    root7.left = TreeNode(3)
    root7.right = TreeNode(7)
    
    print("Before deletion:")
    print("In-order:", inorder_traversal(root7))
    
    root7 = sol.deleteNode(root7, 10)
    print("After trying to delete 10 (not found):")
    print("In-order:", inorder_traversal(root7))
    print_tree(root7)
    
    # Test Case 8: Empty tree
    print("\n" + "=" * 50)
    print("Test 8 - Delete from empty tree")
    root8 = None
    root8 = sol.deleteNode(root8, 5)
    print("Result:", root8)
    
    # Test Case 9: Delete multiple nodes sequentially
    print("\n" + "=" * 50)
    print("Test 9 - Delete multiple nodes [4, 2, 6]")
    root9 = TreeNode(5)
    root9.left = TreeNode(3)
    root9.right = TreeNode(7)
    root9.left.left = TreeNode(2)
    root9.left.right = TreeNode(4)
    root9.right.left = TreeNode(6)
    root9.right.right = TreeNode(8)
    
    print("Original tree:")
    print("In-order:", inorder_traversal(root9))
    
    for key in [4, 2, 6]:
        root9 = sol.deleteNode(root9, key)
        print(f"After deleting {key}: {inorder_traversal(root9)}")
    
    print("\nFinal tree structure:")
    print_tree(root9)
    
    # Test Case 10: Delete from larger BST
    print("\n" + "=" * 50)
    print("Test 10 - Delete from larger BST")
    root10 = TreeNode(10)
    root10.left = TreeNode(5)
    root10.right = TreeNode(15)
    root10.left.left = TreeNode(3)
    root10.left.right = TreeNode(7)
    root10.right.left = TreeNode(12)
    root10.right.right = TreeNode(20)
    root10.left.right.left = TreeNode(6)
    root10.left.right.right = TreeNode(8)
    
    print("Original tree:")
    print("In-order:", inorder_traversal(root10))
    print_tree(root10)
    
    root10 = sol.deleteNode(root10, 5)
    print("\nAfter deleting 5:")
    print("In-order:", inorder_traversal(root10))
    print_tree(root10)
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")
