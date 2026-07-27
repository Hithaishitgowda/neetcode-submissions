class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        start = []
        def palindrome(word):
            j = 0
            k = len(word) - 1
            while j < k:
                if word[j]!= word[k]:
                    return False
                j += 1
                k -= 1
            return True

        def backtrack(i):
            if i == len(s):
                output.append(start.copy())
                return
            for j in range(i, len(s)):
                if palindrome(s[i:j+1]):
                    start.append(s[i: j+1])   
                    backtrack(j+1)
                    start.pop()
                
        backtrack(0)
        return output