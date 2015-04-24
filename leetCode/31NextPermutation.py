class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def checkExist(self, num):
        if len(num) == 1:
            return False
        for n in range(len(num)-1):
            if num[n+1] > num[n]:
                return True
        return False
        
    def nextPermutation(self, num):
        if not self.checkExist(num):
            num[::1] = num[::-1]
            return num
        else:
            for n in range(len(num)-1, 0, -1):
                if num[n-1]<num[n]:
                    firstRuin = n-1
                    break
            #the farest larger than num[n-1]
            for n in range(len(num)-1, 0, -1):
                if num[n] > num[firstRuin]:
                    num[n], num[firstRuin] = num[firstRuin], num[n]
                    num[firstRuin+1:] = sorted(num[firstRuin+1:])
                    return num
                    

s = Solution()                
print s.nextPermutation([1,2,3])
print s.nextPermutation([3,2,1])
print s.nextPermutation([1,3,2])
print s.nextPermutation([1])

