class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        start,end, summation, maximum = 0,0,0,0
        resStart, resEnd = 0,0
        while end<len(nums):
            summation += nums[end]
            if summation>maximum:
                resStart, resEnd,maximum = start, end, summation
            if summation<0:
                start = end + 1
                summation = 0
            end += 1
        if maximum == 0:
            maximum = max(nums)
        return maximum



#nums = [-1]




class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        middle = len(nums)/2
        firstMax,tmp1 = nums[middle-1],0
        secondMax,tmp2 = nums[middle],0
        for i in xrange(middle-1, -1, -1):
            tmp1 += nums[i]
            firstMax = max(tmp1, firstMax)
        for i in xrange(middle, len(nums), 1):
            tmp2 += nums[i]
            secondMax = max(tmp2, secondMax)
        resMerge = firstMax + secondMax
        resSep = max(self.maxSubArray(nums[:middle]),self.maxSubArray(nums[middle:]))
        return max(resMerge, resSep)

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4,1]
#nums = [-1]
print s.maxSubArray(nums)