class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 

        seen = set()
        hashm = {}

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            if s[right] not in seen:
                seen.add(s[right])
            substring = s[left:right + 1]
            hashm[substring] = (right - left + 1) # + 1 because of python exclusion of stop index
            
        
        return max(hashm.values(), default=0)
            
            
            

            
