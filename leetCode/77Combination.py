class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    #k numbers out of n
    def combine(self, n, k):
        state, res = [], []
        self.combineHelp(n,k,state,res)
        return res

    def combineHelp(self, n, k, state, res):
        if k == 0:
            res.append(state[::-1])
            return 
        if k == n:
            state.extend(range(n,0,-1))
            self.combineHelp(0,0,state,res)
            return
        if k<n:
            for addNum in xrange(n, k-1, -1):
                tmpState = state[::1]
                tmpState.append(addNum)
                self.combineHelp(addNum-1, k-1, tmpState, res)

        
s = Solution()
print s.combine(3,3)
print s.combine(2,2)
        
        
        