class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def fourSum(self, num, target):
        num.sort()
        res = set()
        if len(num) <3:
            return []
        for start in xrange(len(num)-3):
            for start1 in xrange(start+1, len(num)-2, 1):
                usedNum = set()
                for end in xrange(start1+1, len(num),1):
                    if target-num[start]-num[start1]-num[end] in usedNum:
                        usedNum.remove(target-num[start]-num[end]-num[start1])
                        res.add((num[start],num[start1], target-num[start]-num[end]-num[start1], num[end]))
                    else:
                        usedNum.add(num[end])
        res1 = [list(r) for r in res]
        return res1

s = Solution()
arr = [1,0,-1,0,-2,2]
print s.fourSum(arr, 0)