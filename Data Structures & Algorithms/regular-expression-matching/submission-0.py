class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            if j + 1 < len(p) and p[j + 1] == "*":

                skip = dfs(i, j + 2)

                use = False

                if match:
                    use = dfs(i + 1, j)

                memo[(i, j)] = skip or use

            else:
                if match:
                    memo[(i, j)] = dfs(i + 1, j + 1)
                else:
                    memo[(i, j)] = False

            return memo[(i, j)]

        return dfs(0, 0)