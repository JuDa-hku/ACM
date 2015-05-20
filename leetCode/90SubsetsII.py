from collections import defaultdict
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        numsDict = defaultdict(int)
        for num in nums:
            numsDict[num] += 1
        elems = [i for i in numsDict]
        elems.sort()
        C, sol = [], []
        self.subsetsWithDupHelp(numsDict, elems, sol, C)
        return C

    def subsetsWithDupHelp(self, numsDict, elems, sol, C):
        if len(elems) == 0:
            C.append(sol)
            return
        for i in xrange(0,numsDict[elems[0]]+1,1):
            tmp,tmpElems = sol[::1], elems[::1]
            tmpElems.pop(0)
            tmp.extend([elems[0]]*i)
            self.subsetsWithDupHelp(numsDict, tmpElems, tmp, C)
        
            
s = Solution()
print s.subsetsWithDup([])