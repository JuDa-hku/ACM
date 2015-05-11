class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        eleList = range(1,n+1,1)
        sol = []
        res = []
        res1 = []
        self.getPermutationHelp(eleList, sol, k, res, res1)
        return ''.join([str(i) for i in res1[0]])
        
    def getPermutationHelp(self, eleList, sol, k, res, res1):
        if len(eleList) == 0:
            res.append(1)
            if len(res) == k:
                res1.append(sol)
        for ele in eleList:
            if res1:
                return
            tmpList,tmpSol = eleList[::1], sol[::1]
            tmpList.remove(ele)
            tmpSol.append(ele)
            self.getPermutationHelp(tmpList, tmpSol, k, res, res1)




class Solution:
    def getPermutation(self, n, k):
        eleList = range(1, n+1, 1)
        return self.getPermutationHelp(eleList, k)
    
    def getPermutationHelp(self, eleList, k):
        i,n = 0,len(eleList)
        if n == 1:
            return str(eleList[0])
        if k==0:
            return ''.join([str(i) for i in eleList])
        while (i+1)*self.factorial(n-1)<k:
            i += 1
        k = k-i*self.factorial(n-1)
        tmp = eleList[i]
        eleList.remove(eleList[i])
        return str(tmp)+self.getPermutationHelp(eleList,k)
            
    def factorial(self, n):
        if n == 0:
            return 0
        if n==1:
            return n
        else:
            return n*self.factorial(n-1)

s = Solution()
print s.getPermutation(2, 1)
        