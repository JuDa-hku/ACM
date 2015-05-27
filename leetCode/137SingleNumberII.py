class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        t, c = 0, 0
        for num in nums:
            tmpT = (num&~c&~t)|(t&~num)
            c = (c&~num) | (t&num&~c)
            t = tmpT
        return t

s = Solution()
print s.singleNumber([3,3,3,10])
