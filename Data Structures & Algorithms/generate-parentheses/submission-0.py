class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        start = []
        def backtrack(open_count, close_count):
            if open_count == n and close_count == n:
                output.append("".join(start))
                return

            if open_count < n:
                start.append('(')
                backtrack(open_count + 1, close_count)
                start.pop()

            if close_count < open_count:
                start.append(")")
                backtrack(open_count, close_count + 1)
                start.pop()


        backtrack(0,0)
        return output