class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        final = []
        for x in nums:
            if x not in freq:
                freq[x] = 0
            freq[x] += 1
        return sorted(freq, key = freq.get, reverse = True)[:k]
        # sorted(iterable, key=None(comparison, optional), reverse=False)
        # reverse = False: ascending, True = descending


