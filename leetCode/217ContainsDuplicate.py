class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numDict = {}
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = 1
        return False
        