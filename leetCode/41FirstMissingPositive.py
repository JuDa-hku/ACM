import collections
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        numDict = collections.defaultdict(int)
        maxium = max(nums)
        if maxium<=0:
            return 1
        for num in nums:
            if num>0:
                numDict[num] = 1
        for key in xrange(1, maxium+2,1):
            if numDict[key] == 0:
                return key

s = Solution()
print s.firstMissingPositive([1,2,0])
print s.firstMissingPositive([3,4,-1,1])
print s.firstMissingPositive([])
print s.firstMissingPositive([1])
print s.firstMissingPositive([0])
        