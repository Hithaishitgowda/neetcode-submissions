class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for u in range(n+1):
            output.append(format(u,'b').count('1'))
        return output