class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = len(text1)
        y = len(text2)
        dp = {}

        def func(i, j):
            if i == x or j == y:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + func(i + 1, j + 1)
            else:
                dp[(i, j)] = max(func(i + 1, j), func(i, j + 1))

            return dp[(i, j)]

        return func(0, 0)