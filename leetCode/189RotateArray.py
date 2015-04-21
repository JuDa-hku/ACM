class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if len(nums)==0 or len(nums)==1:
            return
        while k>len(nums):
            k = k%len(nums)
        appendNums = []
        for i in range(k):
            num = nums.pop()
            nums.insert(0, num)
        
a = Solution()
nums = [1,2,3,4,5,6,7]
num1 = [1]
num0 =[]
a.rotate(nums, 3)
a.rotate(num1,1)
a.rotate(num0,10)