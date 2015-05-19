class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        m, n = len(haystack), len(needle)
        if n>m:
            return -1
        for i in range(0, m-n+1):
            if haystack[i:n+i:1] == needle:
                return i
        return -1

s = Solution()
print s.strStr('a','a')