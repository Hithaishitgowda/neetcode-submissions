class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output = []
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,visited):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited:
                return

            visited.add((r,c))

            up = (r,c+1) 
            down = (r,c-1) 
            right = (r+1,c) 
            left = (r-1,c)

            for (x,y) in [up,down,right,left]:
                if x < rows and x >= 0 and y < cols and y >= 0 and heights[x][y] >= heights[r][c]:
                    dfs(x,y,visited)

        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    output.append([i,j])
        return output