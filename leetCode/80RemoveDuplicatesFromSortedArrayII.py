class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        duplicateFlag, numConsider = False, nums[0]-1
        res = 0
        for num in nums:
            if num == numConsider and duplicateFlag:
                continue
            elif num == numConsider and not duplicateFlag:
                duplicateFlag = True
                nums[res] = num
                res += 1
            elif num != numConsider:
                numConsider = num
                duplicateFlag = False
                nums[res] = num
                res += 1
        return res

s = Solution()
nums = [1,1,1,2,2,3]
nums = [0,1,2,2,2,3]
print s.removeDuplicates(nums)            
        