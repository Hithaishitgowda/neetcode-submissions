from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])

        def bfs():
            count = 0
            while queue:
                x,y,count = queue.popleft()
                if x >= rows or x < 0 or y>= cols or y<0 or grid[x][y]== 0:
                    continue
                
                up = (x,y-1,count+1)
                down = (x,y+1,count+1)
                right = (x+1,y,count+1)
                left = (x-1,y,count+1)

                for neighbour in [up,down,right,left]:
                    a,b,bleh = neighbour
                    if neighbour not in queue and a < rows and a >= 0 and b < cols and b >= 0 and grid[a][b] != 0 and grid[a][b] != 2:
                        grid[a][b] = 2
                        queue.append(neighbour)
            return count

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    start = (i,j,0)
                    queue.append(start)
                
        minutes = bfs()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return minutes
        