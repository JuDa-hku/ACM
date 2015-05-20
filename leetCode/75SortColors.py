class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        i, j, k = 0, 0, len(nums)-1
        while j<=k:
            if nums[j] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                i = i+1
                j = j+1
            elif nums[j] == 1:
                j = j+1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k = k - 1
                

s = Solution()
nums = [0,1,0,2,1,0]
s.sortColors(nums)