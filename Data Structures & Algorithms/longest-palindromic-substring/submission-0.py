class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(n):
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
                    return s[m:k+1]
        p = ""
        for x in range(len(s)):
            res = palindrome(x)
            if res:
                if len(palindrome(x)) > len(p):
                    p = palindrome(x)

        return p
