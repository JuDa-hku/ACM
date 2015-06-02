class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        n = len(nums)
        if n <= 2:
            return min(nums)
        middle = n/2
        if nums[0]<nums[n-1]:
            return nums[0]
        else:
            if nums[middle]<nums[n-1]:
                return self.findMin(nums[:middle+1])
            if nums[middle]>nums[0]:
                return self.findMin(nums[middle+1:])

                

        