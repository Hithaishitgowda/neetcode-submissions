class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(node):
            x, y = node
            if x >= rows or x < 0 or y >= cols or y < 0 or (x,y) in visited or grid[x][y] == '0':
                return
            visited.add(node) 
            up = (x, y-1)
            down = (x, y+1)
            right = (x+1, y)
            left = (x-1, y)

            for neighbour in [up, down, left, right]:
                dfs(neighbour)

        for i in range(rows):
            for j in range(cols):
                start = (i,j)

                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    dfs(start)
                
        return count
        
