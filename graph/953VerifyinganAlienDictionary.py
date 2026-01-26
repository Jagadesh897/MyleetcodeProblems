from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        a = 0
        for i in order:
            a += 1
            dic[i] = a
      
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if dic[w1[j]] > dic[w2[j]]:
                        return False
                    break
                j +=1
            
            if j == len(w2) and j < len(w1):
                return False
                

        return True

# Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: LeetCode Example 1 - Sorted
    print("=" * 60)
    print("Test 1 - LeetCode Example (Sorted)")
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    result1 = sol.isAlienSorted(words1, order1)
    print(f"Words: {words1}")
    print(f"Order: {order1}")
    print(f"Is Sorted: {result1}")  # Expected: True
    
    # Test Case 2: LeetCode Example 2 - Not Sorted
    print("\n" + "=" * 60)
    print("Test 2 - LeetCode Example (Not Sorted)")
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    result2 = sol.isAlienSorted(words2, order2)
    print(f"Words: {words2}")
    print(f"Order: {order2}")
    print(f"Is Sorted: {result2}")  # Expected: False
    
    # Test Case 3: LeetCode Example 3 - Prefix issue
    print("\n" + "=" * 60)
    print("Test 3 - Prefix Issue (apple vs app)")
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    result3 = sol.isAlienSorted(words3, order3)
    print(f"Words: {words3}")
    print(f"Order: {order3}")
    print(f"Is Sorted: {result3}")  # Expected: False (apple > app)
    
    # Test Case 4: Single word
    print("\n" + "=" * 60)
    print("Test 4 - Single word")
    words4 = ["hello"]
    order4 = "abcdefghijklmnopqrstuvwxyz"
    result4 = sol.isAlienSorted(words4, order4)
    print(f"Words: {words4}")
    print(f"Order: {order4}")
    print(f"Is Sorted: {result4}")  # Expected: True
    
    # Test Case 5: Two identical words
    print("\n" + "=" * 60)
    print("Test 5 - Two identical words")
    words5 = ["hello", "hello"]
    order5 = "abcdefghijklmnopqrstuvwxyz"
    result5 = sol.isAlienSorted(words5, order5)
    print(f"Words: {words5}")
    print(f"Order: {order5}")
    print(f"Is Sorted: {result5}")  # Expected: True
    
    # Test Case 6: Reversed alphabet order
    print("\n" + "=" * 60)
    print("Test 6 - Reversed alphabet (z comes first)")
    words6 = ["zyx", "abc"]
    order6 = "zyxwvutsrqponmlkjihgfedcba"
    result6 = sol.isAlienSorted(words6, order6)
    print(f"Words: {words6}")
    print(f"Order: {order6}")
    print(f"Is Sorted: {result6}")  # Expected: True
    
    # Test Case 7: Completely different order
    print("\n" + "=" * 60)
    print("Test 7 - Custom order sorted correctly")
    words7 = ["kuvp", "q"]
    order7 = "ngxlkthsjuoqcpavbfdermiywz"
    result7 = sol.isAlienSorted(words7, order7)
    print(f"Words: {words7}")
    print(f"Order: {order7}")
    print(f"Is Sorted: {result7}")  # Expected: True
    
    # Test Case 8: Multiple words sorted
    print("\n" + "=" * 60)
    print("Test 8 - Multiple words sorted")
    words8 = ["app", "apple", "banana"]
    order8 = "abcdefghijklmnopqrstuvwxyz"
    result8 = sol.isAlienSorted(words8, order8)
    print(f"Words: {words8}")
    print(f"Order: {order8}")
    print(f"Is Sorted: {result8}")  # Expected: True
    
    # Test Case 9: First character difference
    print("\n" + "=" * 60)
    print("Test 9 - First character difference (not sorted)")
    words9 = ["banana", "apple"]
    order9 = "abcdefghijklmnopqrstuvwxyz"
    result9 = sol.isAlienSorted(words9, order9)
    print(f"Words: {words9}")
    print(f"Order: {order9}")
    print(f"Is Sorted: {result9}")  # Expected: False
    
    # Test Case 10: Single character words
    print("\n" + "=" * 60)
    print("Test 10 - Single character words")
    words10 = ["a", "b", "c"]
    order10 = "abcdefghijklmnopqrstuvwxyz"
    result10 = sol.isAlienSorted(words10, order10)
    print(f"Words: {words10}")
    print(f"Order: {order10}")
    print(f"Is Sorted: {result10}")  # Expected: True
    
    # Test Case 11: Single character words not sorted
    print("\n" + "=" * 60)
    print("Test 11 - Single character words (not sorted)")
    words11 = ["c", "b", "a"]
    order11 = "abcdefghijklmnopqrstuvwxyz"
    result11 = sol.isAlienSorted(words11, order11)
    print(f"Words: {words11}")
    print(f"Order: {order11}")
    print(f"Is Sorted: {result11}")  # Expected: False
    
    # Test Case 12: Edge case with prefix
    print("\n" + "=" * 60)
    print("Test 12 - Correct prefix order (app before apple)")
    words12 = ["app", "apple"]
    order12 = "abcdefghijklmnopqrstuvwxyz"
    result12 = sol.isAlienSorted(words12, order12)
    print(f"Words: {words12}")
    print(f"Order: {order12}")
    print(f"Is Sorted: {result12}")  # Expected: True
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")