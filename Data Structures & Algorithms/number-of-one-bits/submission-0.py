class Solution:
    def hammingWeight(self, n: int) -> int:
        def dnq(a,b):
            if a==b:
                return (n>>a) & 1
            m = (a+b) // 2
            left = dnq(a,m)
            right = dnq(m+1,b)
            return (left+right)

        return dnq(0,31)
