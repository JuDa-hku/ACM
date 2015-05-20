class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        res = []
        if len(nums) == 1:
            return [[nums[0]], []]
        tmpRes = self.subsets(nums[:-1])
        for sub in tmpRes:
            tmpsub = sub[::1]
            tmpsub.append(nums[-1])
            res.append(tmpsub)
        res.extend(tmpRes)
        return res

s = Solution()
print len(s.subsets([1,2,3,4]))
print (s.subsets([4,1,0]))