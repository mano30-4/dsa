class Solution:
    def trailingZeroes(self, n: int) -> int:
     def num_of_zeros(n):
            if n < 5:
                return 0

            return n // 5 + num_of_zeros(n // 5)
     return num_of_zeros(n)
"""
Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:
Input: n = 0
Output: 0
"""