class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = set()
        if len(num) <3:
            return []
        for start in xrange(len(num)-2):
            usedNum = set()
            for end in xrange(start+1, len(num),1):
                if -num[start]-num[end] in usedNum:
                    usedNum.remove(-num[start]-num[end])
                    res.add((num[start],  -num[start]-num[end], num[end]))
                else:
                    usedNum.add(num[end])
        res1 = [list(r) for r in res]
        return res1

s = Solution()
arr = range(10,-2,-1)
arr = [0,0,0]
print s.threeSum(arr)