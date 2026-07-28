class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            s = (a ^ b) & mask
            c = ((a & b) << 1) & mask

            a = s
            b = c

        if a > 0x7FFFFFFF:
            return a - 0x100000000

        return a