class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        currentFar, nextFar = 0, 0
        for i,n in enumerate(nums):
            if i<=currentFar:
                nextFar = max(nextFar, i+n)
            if nextFar>=len(nums)-1:
                return True
            currentFar = nextFar
        if currentFar<len(nums)-1:
            return False



class Solution:
    def canJump(self, nums):
        currentFar, nextFar,i = 0, 0,0
        while currentFar<len(nums)-1:
            while i<= currentFar:
                nextFar = max(nums[i]+i, nextFar)
                i += 1
            if nextFar == currentFar:
                return False
            currentFar = nextFar
        return True
            
s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])
print s.canJump([0])
print s.canJump([1,1,2,2,0,1,1])            

                