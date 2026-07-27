class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        start = []
        phone = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        if not digits:
            return []
        def backtrack(i):
            if i == len(digits):
                output.append("".join(start))
                return
            for j in phone[digits[i]]:
                start.append(j)
                backtrack(i+1)
                start.pop()
        backtrack(0)
        return output
            
