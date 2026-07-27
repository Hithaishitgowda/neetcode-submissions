class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(node, visited2):
            x, y = node
            if x>=rows or x<0 or y>=cols or y<0 or (x,y) in visited or grid[x][y] == 0:
                return

            visited.add(node)
            visited2.add(node)

            up = (x,y-1)
            down = (x,y+1)
            right = (x+1,y)
            left = (x-1,y)

            for neighbour in [up,down,right,left]:
                dfs(neighbour, visited2)
            count2 = len(visited2)
            return count2
            
        for i in range(rows):
            for j in range(cols):
                start = (i,j)

                if grid[i][j] == 1 and (i,j) not in visited:
                    visited2 = set()
                    count = max(count,dfs(start,visited2))

        return count