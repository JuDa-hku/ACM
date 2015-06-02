class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        n = len(nums)
        if len(nums)<2:
            return 0
        gap = 0
        MAX, MIN = max(nums), min(nums)
        interval = float(MAX-MIN)/n
        container = [None]*n
        for i in xrange(n):
            container[i] = set()

        for num in nums:
            idx = min(int((num-MIN)/interval), n-1)
            container[idx].add(num)

        res, last = 0, 0
        for i in range(0,n):
            if len(container[i]):
                res = max(res, min(container[i])- max(container[last]))
                last = i
        return res
                    
s= Solution()
print s.maximumGap([1,1,1,1,1,5,5,5,5,5])