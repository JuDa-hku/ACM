class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        jumpList,n = [], len(nums)
        for i in xrange(n):
            jumpList.append(nums[i]+i)
#        print jumpList
        maximumEnd,step,startIndex = jumpList[0],1,0
        while maximumEnd < n-1:
            step += 1
#            print maximumEnd
            tmpMax,tmpIndex = 0,0
            for i,num in enumerate(jumpList[startIndex:maximumEnd+1]):
                i = i + startIndex
                if num>=tmpMax:
                    tmpMax, tmpIndex = num, i
            startIndex, maximumEnd = tmpIndex, tmpMax
#            print startIndex, maximumEnd
        return step

s = Solution()
print s.jump([2,3,1,1,4])
print s.jump([100,3,1,1,4])
print s.jump([5,9,3,2,1,0,2,3,3,1,0,0])
print s.jump([1,1,1,1])
print s.jump([2,3,5,9,0,9,7,2,7,9,1,7,4,6,2,1,0,0,1,4,9,0,6,3])

#nums = [1] * 100000
#print s.jump(nums)