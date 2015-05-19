class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        n = len(nums)
        if n==0:
            return False
        return self.searchHelp(nums, target, 0, n-1)

    def searchHelp(self, nums, target, start, end):
        middle = (start+end)/2
        
        if target ==nums[start]:
            return True
        if target ==nums[end]:
            return True
        if target ==nums[middle]:
            return True
        if end-start <= 1:
            return False

        if nums[start] == nums[end]:
            return self.searchHelp(nums, target, start, end-1)


        if nums[middle]>=nums[end] and nums[middle]>=nums[start]:
            if target<nums[middle] and target>nums[start]:
                return self.searchHelp(nums, target, start, middle)
            if target<nums[middle] and target<nums[end]:
                return self.searchHelp(nums, target, middle, end)
            if target>nums[middle]: 
                return self.searchHelp(nums, target, middle, end)
            else:
                return False


        if nums[middle]<=nums[end] and nums[middle]<=nums[start]:
            if target<nums[middle]:
                return self.searchHelp(nums, target, start, middle)
            if target>nums[middle] and target<nums[end]:
                return self.searchHelp(nums, target, middle, end)
            if target>nums[middle] and target>=nums[end]:
                return self.searchHelp(nums, target, start, middle)

        if nums[middle]<=nums[end] and nums[middle]>=nums[start]:
            if target<nums[middle]:
                return self.searchHelp(nums, target, start, middle)
            if target>=nums[middle]:
                return self.searchHelp(nums, target, middle, end)

s = Solution()
nums = [1,3,1,1,1]
for i in range(9):
    print s.search(nums, i)