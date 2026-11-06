class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        ij = []

        for index, value in enumerate(nums):
            need = target - value
            if need in hashmap:
                ij.append(index)
                ij.append(hashmap[need]) 
                return sorted(ij)
            else:
                hashmap[value] = index
        return False
        


        