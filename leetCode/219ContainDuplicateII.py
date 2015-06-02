class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numsDict = {}
        for i in xrange(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = [i]
            else:
                for j in numsDict[nums[i]]:
                    if i-j<=k:
                        return True
                numsDict[nums[i]].append(i)
        return False

                    