class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        s = sorted(s) 
        t = t.lower()
        t = sorted(t) 
        if ( s == t ):
            return True
        return False