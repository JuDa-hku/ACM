class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        if len(s) == 0 or self.isPalindrome(s):
            return 0
        
        dp = [len(s)-1]*(len(s)+1)
        dp[0], dp[1] = 0, 0
        
        for i in xrange(len(s)):
            dp[i+1] = min(dp[i+1], dp[i]+1)
            for j in xrange(i):
                if j==0 and self.isPalindrome(s[0:i+1]):
                    dp[i+1] = 0
                elif self.isPalindrome(s[j:i+1]):
                    dp[i+1] = min(dp[i+1], dp[j]+1)
                if dp[i+1] == 0 or dp[i+1]==1:
                    break
        return dp[len(s)]



    def isPalindrome(self, s):
        return s == s[::-1]



## the shortest path solution.
from collections import deque:
class Solution:
    def minCut(self, s):
        palindrome = [{i+1} for i in range(len(s)) ]
        for i in range(len(s)):
            j = 0
            while i>=j and i+j+1<len(s) and s[i-j] == s[i+j+1]:
                palindrome[i-j].add(i+j+2)
                j += 1
            j = 1
            while i>=j and i+j<len(s) and s[i-j] = s[i+j]:
                palindrome[i-j].add(i+j+1)
                j += 1

        cut, visited = 0, set([0])
        q = deque
        q.append((0,0))
        while q:
            i, cut = q.popleft()
            for j in palindrome[i]:
                if j == len(s):
                    return cut
                elif j not in visited:
                    q.append((j, cut+1))
                    visited.add(j)

        return cut

s = Solution()
print s.minCut("a"*10000)