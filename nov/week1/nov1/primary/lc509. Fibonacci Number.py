class Solution:
    def fib(self, n: int) -> int:
        def f(n):
            if n <= 1:
                return n

            return f(n - 1) + f(n - 2)
        return f(n)
"""
Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
"""
