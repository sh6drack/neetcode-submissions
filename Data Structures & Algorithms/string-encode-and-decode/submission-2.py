class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for x in strs:
            result += str(len(x)) + "*" + x
        return result

#could also just return with a joined hash and remove the hsh but the case where there was already that particular hash or character will make it fail

    def decode(self, s: str) -> List[str]:
        result = [] # so append adds to list
        i = 0
        while i < len(s):
            j = s.find("*", i)
            n = int(s[i:j])
            result.append(s[j+1:j+1+n])
            i = j+1+n
        return result

#word starts at j + 1 and ends at j + 1 + n



