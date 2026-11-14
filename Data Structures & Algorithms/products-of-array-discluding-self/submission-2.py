class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

    #    for i in nums:
    #        val = 1
    #        for x in range(len(nums)):
    #            if nums[x] == i:
    #                continue
    #            val *= nums[x]
    #        flist.append(val)
        n = len(nums)

        flist = [1] * n

        prefix = 1
        for i in range(n):
            flist[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1): # (START, STOP, STEP) start = n-1 to start at the last index, stop -1 so it doesnt go infintiely back, step by a decrease of -1
            flist[i] *= suffix
            suffix *= nums[i]
        
        return flist

