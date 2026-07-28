import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue

                if (nr, nc) in visited:
                    continue

                newTime = max(time, grid[nr][nc])

                heapq.heappush(heap, (newTime, nr, nc))
        