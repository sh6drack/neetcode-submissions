class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
     s = s.lower()
     t = t.lower()

     sl = len(s)
     tl = len(t)

     if sl != tl:
        return False

     return sorted(s) == sorted(t)