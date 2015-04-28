class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        if len(nums) == 1 and nums[0] >= target:
            return 0
        if len(nums) == 1 and nums[0] < target:
            return 1
        mid = len(nums)/2-1
#        print mid, nums
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        if nums[mid] < target:
            return mid+1+self.searchInsert(nums[mid+1:],target)

s = Solution()
a = [1,3,5,6]
for t in range(7):
    print s.searchInsert(a,t), t