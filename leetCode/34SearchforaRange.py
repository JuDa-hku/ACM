class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def leftMostSearch(self, nums, target):
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        if n== 2 and nums[0] == target:
            return 0
        if n== 2 and nums[1] == target:
            return 1
        if nums[n/2] == target:
            return self.leftMostSearch(nums[:n/2+1], target)
        if nums[n/2] < target:
            return n/2+1+self.leftMostSearch(nums[n/2+1:], target)
            
    def rightMostSearch(self, nums, target):
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        if n== 2 and nums[1] == target:
            return 1
        if n== 2 and nums[0] == target:
            return 0
        if nums[n/2] == target:
            return n/2+self.rightMostSearch(nums[n/2:], target)
        if nums[n/2] > target:
            return self.rightMostSearch(nums[:n/2], target)            
    
    def searchRange(self, nums, target):
        n = len(nums)
        if n == 0:
            return [-1,-1]
        if nums[n/2] == target:
            left = self.leftMostSearch(nums[:n/2+1], target)
            right = n/2+self.rightMostSearch(nums[n/2:], target)
            return [left, right]
        if nums[n/2] < target:
            res = self.searchRange(nums[n/2+1:], target)
            if res[0] != -1:
                res[0], res[1] = res[0]+n/2+1, res[1]+n/2+1
        if nums[n/2] > target:
            res = self.searchRange(nums[:n/2], target)
        return res

s = Solution()
nums = [0,0,0,2,3,5,5]
print s.leftMostSearch(nums, 5)
print s.rightMostSearch(nums, 0)
nums = [5,7,7,8,8,10]
print s.searchRange(nums, 9)
print s.searchRange([1,2,3], 3)