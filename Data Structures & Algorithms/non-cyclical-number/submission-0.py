class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}

        while n != 1:
            if n in d:
                return False

            d[n] = 1

            sum1 = 0
            for i in str(n):
                sum1 += int(i) ** 2

            n = sum1

        return True

        