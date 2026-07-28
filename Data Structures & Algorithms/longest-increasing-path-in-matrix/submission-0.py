class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            longest = 1

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if matrix[nr][nc] <= matrix[r][c]:
                    continue

                longest = max(longest, 1 + dfs(nr, nc))

            memo[(r, c)] = longest

            return longest

        result = 0

        for r in range(rows):
            for c in range(cols):
                result = max(result, dfs(r, c))

        return result
        