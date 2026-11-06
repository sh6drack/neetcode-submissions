class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     s = s.lower()
     t = t.lower()

     if len(s) != len(t):
        return False
     for x in s:
        if s.count(x) != t.count(x):
            return False
     return True
    