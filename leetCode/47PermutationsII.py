class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        C,D = set(),set()
        return [list(t) for t in self.permuteUniqueHelp([], num, C, D)]


    def permuteUniqueHelp(self,solution, num, C, D):
        if len(num) == 0:
            C.add(tuple(solution))
            return
        tmp = num[:]
        for n in set(tmp):
            tmp1 = solution[:]
            tmp1.append(n)
            tmp2 = num[:]
            tmp2.remove(n)
            self.permuteUniqueHelp(tmp1, tmp2, C, D)
        return C


s = Solution()
#print s.permuteUnique([3,3,0,0,2,3,2])
print s.permuteUnique([1,1,2,2])