class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        sol,res = [],[]
        self.combinationSum3Help(k,n,res,sol)
        return res

    def combinationSum3Help(self, k, n, res, sol):
        if k==0 and n==0:
            res.append(sol)
            return
        elif k>0 and n>0:
            if len(sol) == 0:
                for i in range(1,10):
                    tmp = sol[::]
                    tmp.append(i)
                    self.combinationSum3Help(k-1, n-i, res, tmp)
            else:
                for i in range(sol[-1]+1, 10):
                    tmp = sol[::]
                    tmp.append(i)
                    self.combinationSum3Help(k-1, n-i, res, tmp)                    
                    
        else:
            return

            
    
s = Solution()
print s.combinationSum3(2, 18)