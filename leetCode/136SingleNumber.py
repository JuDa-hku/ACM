class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res = res^num
        return res

s = Solution()
print s.singleNumber([4,2,2,3,4])