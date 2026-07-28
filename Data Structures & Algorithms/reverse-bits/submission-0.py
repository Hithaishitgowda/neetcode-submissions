class Solution:
    def reverseBits(self, n: int) -> int:
        m = format(n, '032b') 
        m = m[::-1]           
        return int(m, 2)       