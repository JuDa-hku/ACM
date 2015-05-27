class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n, res,secondRes = len(s), [],[]
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        for i in xrange(n):
            if self.isPalindrome(s[:i+1]):
                first = [s[:i+1]]
                secondRes = self.partition(s[i+1:])
                for resS in secondRes:
                        tmp = first + resS
                        res.append(tmp)
        return res

    def isPalindrome(self, s):
        return s == s[::-1]



s = Solution()
print s.partition("bb")
print s.partition("seeslaveidemon")
        