class Solution:
    def reverse(self, x: int) -> int:
        m = str(x)
        n = m.strip('-')
        n = n[::-1]
        o = int(n)
        if o > (2**31) - 1:
            return 0
        if x < 0:
            return -o
        return o