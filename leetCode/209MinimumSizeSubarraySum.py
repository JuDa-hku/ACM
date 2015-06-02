class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if sum(nums)<s:
            return 0
        n = len(nums)
        res, start, end, summation = n,0,0,0
        while end<=n-1:
            summation += nums[end]
            while summation>=s:
                res = min(res, end-start+1)
                summation -= nums[start]                
                start += 1
            end += 1
        return res

s = Solution()
print s.minSubArrayLen(7, [2,3,1,2,4,3])
