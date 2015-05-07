class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        res, C = [], []
        self.permuteHelp(nums, res, C)
        return C
        

    def permuteHelp(self, nums,res, C):
        if len(nums) == 0:
            C.append(res)
            return
        for num in nums:
            tmpNum, tmpRes = nums[:], res[:]
            tmpNum.remove(num)
            tmpRes.append(num)
            self.permuteHelp(tmpNum,tmpRes,C)
            
        
        
s = Solution()
print s.permute([1,2,3])