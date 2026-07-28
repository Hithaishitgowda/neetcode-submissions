class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits)-1
        output = []
        total = digits[j]+1
        s = total % 10
        c = total // 10
        digits[j] = s
        j -= 1
        while c and j >= 0:
            total = digits[j] + c 
            s = total % 10
            c = total // 10
            digits[j] = s
            j -= 1

        if c:
            digits.insert(0,c)

        return digits