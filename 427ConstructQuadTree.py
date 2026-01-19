from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.helper(grid,0,0,len(grid))
    
    def helper(self,grid,i,j,w):
        if self.issame(grid,i,j,w):
            return Node(grid[i][j] == 1,True,None, None, None, None)
        node = Node(True, False, None, None, None, None) 
        node.topLeft = self.helper(grid,i, j ,w//2)
        node.topRight = self.helper(grid,i ,j + w //2 , w//2)
        node.bottomLeft = self.helper(grid,i + w//2, j ,w//2)
        node.bottomRight = self.helper(grid,i + w//2,j + w//2,w//2)
        return node

    def issame(self,grid,i,j,w):
        for x in range(i,i + w):
            for y in range(j, j + w):
                if grid[x][y] != grid[i][j]:
                    return False
        return True

# Helper function to convert QuadTree to list representation
def quad_tree_to_list(node):
    """
    Converts QuadTree to LeetCode's list format:
    [[isLeaf, val], ...]
    """
    if not node:
        return []
    
    result = []
    queue = [node]
    
    while queue:
        current = queue.pop(0)
        if current is None:
            continue
        
        result.append([current.isLeaf, 1 if current.val else 0])
        
        if not current.isLeaf:
            queue.append(current.topLeft)
            queue.append(current.topRight)
            queue.append(current.bottomLeft)
            queue.append(current.bottomRight)
    
    return result

# Helper function to print the QuadTree structure
def print_quad_tree(node, level=0, position="Root"):
    if node is None:
        return
    
    indent = "  " * level
    val_str = "1" if node.val else "0"
    leaf_str = "Leaf" if node.isLeaf else "Internal"
    print(f"{indent}{position}: val={val_str}, isLeaf={node.isLeaf} ({leaf_str})")
    
    if not node.isLeaf:
        print_quad_tree(node.topLeft, level + 1, "TopLeft")
        print_quad_tree(node.topRight, level + 1, "TopRight")
        print_quad_tree(node.bottomLeft, level + 1, "BottomLeft")
        print_quad_tree(node.bottomRight, level + 1, "BottomRight")

# Helper to print grid
def print_grid(grid):
    for row in grid:
        print("  " + " ".join(str(x) for x in row))

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Mixed 2x2 grid
    print("=" * 60)
    print("Test 1 - Mixed 2x2 grid")
    grid1 = [
        [0, 1],
        [1, 0]
    ]
    print("Grid:")
    print_grid(grid1)
    result1 = sol.construct(grid1)
    print("\nQuadTree Structure:")
    print_quad_tree(result1)
    print(f"List format: {quad_tree_to_list(result1)}")
    
    # Test Case 2: LeetCode Example - 4x4 mixed grid
    print("\n" + "=" * 60)
    print("Test 2 - LeetCode Example 4x4 grid")
    grid2 = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]
    ]
    print("Grid (8x8):")
    print_grid(grid2)
    result2 = sol.construct(grid2)
    print("\nQuadTree Structure:")
    print_quad_tree(result2)
    
    # Test Case 3: All zeros - single leaf
    print("\n" + "=" * 60)
    print("Test 3 - All zeros (single leaf)")
    grid3 = [
        [0, 0],
        [0, 0]
    ]
    print("Grid:")
    print_grid(grid3)
    result3 = sol.construct(grid3)
    print("\nQuadTree Structure:")
    print_quad_tree(result3)
    print(f"List format: {quad_tree_to_list(result3)}")
    
    # Test Case 4: All ones - single leaf
    print("\n" + "=" * 60)
    print("Test 4 - All ones (single leaf)")
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    print("Grid:")
    print_grid(grid4)
    result4 = sol.construct(grid4)
    print("\nQuadTree Structure:")
    print_quad_tree(result4)
    print(f"List format: {quad_tree_to_list(result4)}")
    
    # Test Case 5: 1x1 grid with 0
    print("\n" + "=" * 60)
    print("Test 5 - 1x1 grid with 0")
    grid5 = [[0]]
    print("Grid:")
    print_grid(grid5)
    result5 = sol.construct(grid5)
    print("\nQuadTree Structure:")
    print_quad_tree(result5)
    print(f"List format: {quad_tree_to_list(result5)}")
    
    # Test Case 6: 1x1 grid with 1
    print("\n" + "=" * 60)
    print("Test 6 - 1x1 grid with 1")
    grid6 = [[1]]
    print("Grid:")
    print_grid(grid6)
    result6 = sol.construct(grid6)
    print("\nQuadTree Structure:")
    print_quad_tree(result6)
    print(f"List format: {quad_tree_to_list(result6)}")
    
    # Test Case 7: 4x4 checkerboard pattern
    print("\n" + "=" * 60)
    print("Test 7 - 4x4 with top-left quadrant different")
    grid7 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    print("Grid:")
    print_grid(grid7)
    result7 = sol.construct(grid7)
    print("\nQuadTree Structure:")
    print_quad_tree(result7)
    
    # Test Case 8: 4x4 all zeros
    print("\n" + "=" * 60)
    print("Test 8 - 4x4 all zeros")
    grid8 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print("Grid:")
    print_grid(grid8)
    result8 = sol.construct(grid8)
    print("\nQuadTree Structure:")
    print_quad_tree(result8)
    print(f"List format: {quad_tree_to_list(result8)}")
    
    # Test Case 9: Complex 4x4
    print("\n" + "=" * 60)
    print("Test 9 - Complex 4x4 grid")
    grid9 = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]
    print("Grid:")
    print_grid(grid9)
    result9 = sol.construct(grid9)
    print("\nQuadTree Structure:")
    print_quad_tree(result9)
    
    # Test Case 10: Alternating pattern
    print("\n" + "=" * 60)
    print("Test 10 - Alternating quadrants")
    grid10 = [
        [1, 0],
        [0, 1]
    ]
    print("Grid:")
    print_grid(grid10)
    result10 = sol.construct(grid10)
    print("\nQuadTree Structure:")
    print_quad_tree(result10)
    print(f"List format: {quad_tree_to_list(result10)}")
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")