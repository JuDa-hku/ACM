class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        newNums = []
        for num in nums:
            if num != val:
                newNums.append(num)
        res = len(newNums)
        nums[0:res:1] = newNums
        return res