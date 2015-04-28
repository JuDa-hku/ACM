import copy
import timeit
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        solutionList,solution = [], []
        candidates.sort()
        self.combinationSumHelp(0, candidates, target, solution, solutionList)
        return solutionList
        

    def combinationSumHelp(self, start, candidates, target, solution,solutionList):
        minum = min(candidates)
        if target == 0:
            solutionList.append(solution[:])
            return
        if target < minum:
            return
        for i in range(start, len(candidates), 1):
            solution.append(candidates[i])
            self.combinationSumHelp(i,candidates, target-candidates[i], solution, solutionList)
            solution.pop()


s = Solution()
print s.combinationSum([2,3,6,7], 7)
candidates = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
target = 310
print s.combinationSum(candidates, target)