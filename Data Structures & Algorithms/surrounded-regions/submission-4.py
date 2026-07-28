from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        queue = deque()
        ooo = set()

        def bfs():
            while queue:
                x,y = queue.popleft()
                if x>=rows or x<0 or y>=cols or y<0 or (x,y) in visited:
                    continue
                visited.add((x,y))
                up = (x,y+1)
                down = (x,y-1)
                left = (x-1,y)
                right = (x+1,y)
                for k,l in [up,down,right,left]:
                    if k<rows and k>=0 and l<cols and l>=0 and board[k][l] == 'O':
                        ooo.add((k,l))
                        queue.append((k,l))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i == rows-1 or i == 0 or j==cols-1 or j ==0):
                    queue.append((i,j))
                    ooo.add((i,j))
                    bfs()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in ooo:
                    board[i][j] = 'X'

