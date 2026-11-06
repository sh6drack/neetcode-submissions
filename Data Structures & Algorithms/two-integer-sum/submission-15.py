class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # ex: nums = [3,4,5,6]
        for i in range(len(nums)): # range of (0,4)
            for j in range(i + 1, len(nums)): # range of (1,4)
                if nums[i] + nums[j] == target:
                    return [i, j]
        
