
class Solution:
    def longestConsecutive(self, num):
        S = set(num)
        maxLength = 0
        while S:
            n = S.pop()
            lP, lN = 0, 0
            P, N = n+1, n-1
            while P in S:
                S.remove(P)
                lP, P = 1+lP, P+1
            while N in S:
                S.remove(N)
                lN, N = 1+lN, N-1
            maxTmp = lP + lN + 1
            if maxTmp > maxLength:
                maxLength = maxTmp
        return maxLength

s = Solution()
print s.longestConsecutive([100, 4, 400, 1, 3, 2])
            
            

            