from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        def bfs():
            while queue:
                x,y,count = queue.popleft()
                if x >= rows or x < 0 or y >= cols or y < 0 or (x,y) in visited or grid[x][y] == -1:
                    continue

                visited.add((x,y))

                if grid[x][y] == INF:
                    grid[x][y] = count

                up = (x, y-1,count+1)
                down = (x, y+1,count+1)
                right = (x+1, y,count+1)
                left = (x-1, y,count+1)

                for neighbour in [up,down,left,right]:
                    queue.append(neighbour)

        for i in range(rows):
            for j in range(cols):
                start = (i,j,0)
                if grid[i][j] == 0 and (i,j) not in visited:
                    queue.append(start)
        bfs()