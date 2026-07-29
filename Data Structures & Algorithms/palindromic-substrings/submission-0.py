class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def palindrome(n):
            nonlocal count
            for i in range(len(s)-(n)):
                j = i+(n)
                m = i
                k = j
                while i < j:
                    if s[i] != s[j]:
                        break
                    i += 1
                    j -= 1
                else:
                    count += 1
        p = ""
        for x in range(len(s)):
            palindrome(x)

        return count
