class Solution:
    def getNthPentagonalNum(self, n):
        def pentagonal(n):
            if n == 1:
                return 1

            return pentagonal(n - 1) + (3 * n - 2)

        return pentagonal(n)
"""
Input: n = 1 Output: 1 
Input: n = 2 Output: 5 
Input: n = 3 Output: 12 a
"""