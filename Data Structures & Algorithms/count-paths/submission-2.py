class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = {}
        def win(i,j):
            if i == m-1 and j == n-1:
                return 1 
            if i >= m or j >= n:
                return 0
            if (i,j) in visited:
                return visited[(i,j)]
            answer = win(i+1,j) + win(i,j+1)
            visited[(i,j)] = answer
            return answer
        return win(0,0)
            