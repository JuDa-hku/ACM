class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n<=3:
            return max(nums)
        line0 = self.robHelp0(nums[:n-1])
        line1 = self.robHelp0(nums[1:n-2])
#        print line0, line1, nums[:n-1], nums[1:n-2]
        return max(line0, line1+nums[n-1])

    def robHelp0(self, num):
        return self.robHelp(num)

    def robHelp(self, num):
        store = [0]*len(num)
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        store[0] = num[0]
        store[1] = max(num[0], num[1])
        for i in range(2,len(num)):
            numWithi = store[i-2] + num[i]
            numWithouti = store[i-1]
            if numWithi>numWithouti:
                store[i] = numWithi
            else:
                store[i] = numWithouti
        return store[len(num)-1]

s = Solution()        
print s.rob([1,2,3,4])