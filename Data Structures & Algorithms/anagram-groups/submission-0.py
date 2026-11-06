class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashm = {}
        # for each string in listt, count frequency of each character to match against other strings
        for x in strs:
            key = ''.join(sorted(x))
            if key not in hashm:
                hashm[key] = [] #value needs to be a list
            hashm[key].append(x)

        return list(hashm.values())




        