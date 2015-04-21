class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 1
        if n==0:
            return 0
        if n==1:
            return 1
        while n>1:
            flag = n%2
            if flag: count += 1
            n = n/2
        return count

a = Solution()
print a.hammingWeight(3)
print a.hammingWeight(1)
print a.hammingWeight(2)