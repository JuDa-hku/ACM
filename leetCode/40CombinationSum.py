class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        solutionList,solution = [], []
        newCandidates = [num for num in candidates if num<target]
        newCandidates.sort()
        self.combinationSumHelp(0, newCandidates, target, solution, solutionList)
        if target in candidates:
            solutionList.append([target])
        return solutionList
        

    def combinationSumHelp(self, start, candidates, target, solution,solutionList):
        if target == 0:
            if solution not in solutionList:
                solutionList.append(solution[:])
            return
        if target < 0:
            return
        if start == len(candidates):
            return
        mimum = min(candidates[start:])
        if target<mimum:
            return
        ##at first I do not add target<mimum, it has to search too many state.
        solution.append(candidates[start])
        self.combinationSumHelp(start+1,candidates, target-candidates[start], solution, solutionList)
        solution.pop()
        self.combinationSumHelp(start+1,candidates, target, solution, solutionList)


s = Solution()
print s.combinationSum([2], 1)
print s.combinationSum([2,3,6,7], 7)
candidates = [92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73]
target = 310
candidates =[13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]
target = 25
print s.combinationSum(candidates, target)