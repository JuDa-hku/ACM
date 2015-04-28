class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        start, end = 0, len(nums)-1
        while start<end:
            if nums[start+1] > nums[start]:
                start += 1
            elif nums[start+1] < nums[start]:
                return start
            if nums[end] < nums[end-1]:
                end -= 1
            elif nums[end] > nums[end-1]:
                return end
        return start
        
##not log(n), it can be log(n) by using binary search
s = Solution()
print s.findPeakElement([1,2,1])