# class Solution:
#     # @param nums, an integer[]
#     # @return an integer
#     def prod(self, nums):
#         if len(nums) == 0:
#             return -float('inf')
#         result = 1
#         for num in nums:
#             result*=num
#         return result
        
    
#     def maxProductWithoutZero(self, nums):
#         #find the negative number index
#         indexList = []
#         if len(nums) == 1:
#             return nums[0]
#         for i, num in enumerate(nums):
#             if num<0:
#                 indexList.append(i)
#         if len(indexList)%2 == 0:
#             return self.prod(nums)
#         else:
#             return max(self.prod(nums[indexList[0]+1:]), self.prod(nums[:indexList[-1]]))

#     def maxProduct(self, nums):
#         #cut the nums according to 0 position
#         firstPosition = 0
#         secondPosition = len(nums)-1
#         zeroPoition = []
#         res = self.maxProductWithoutZero(nums)
#         for index,num in enumerate(nums):
#             if num == 0:
#                 res = max(res,0)
#                 secondPosition = index
#                 res = max(self.maxProductWithoutZero(nums[firstPosition:secondPosition]), res)
#                 firstPosition = secondPosition + 1
#         res = max(self.maxProductWithoutZero(nums[firstPosition:]), res)
#         return res
                
            
s = Solution()
print s.maxProduct([-2,-3,-2,4])
print s.maxProduct([2,3,-2,4])
print s.maxProduct([0,2,0,0,0,10,3])
print s.maxProduct([0,2])
print s.maxProduct([-4,-3,-2])



class Solution:
    def maxProduct(self, nums):
        res = maxFront = minFront = nums[0]
        for i in range(1,len(nums)):
            maxTmpFront = max(nums[i], maxFront*nums[i], minFront*nums[i])
            minTmpFront = min(nums[i], maxFront*nums[i], minFront*nums[i])
            maxFront = maxTmpFront
            minFront = minTmpFront
            res = max(maxFront, res)
        return res
s = Solution()
print s.maxProduct([-4,-3,-2])