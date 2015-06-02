class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        isIs = {}
        isIs1 = {}
        for chs, cht in zip(s,t):
            if chs in isIs:
                if isIs[chs] != cht:
                    return False
            if cht in isIs1:
                if isIs1[cht] != chs:
                    return False
            isIs[chs] = cht
            isIs1[cht] = chs
        return True

s = Solution()
print s.isIsomorphic("egg", "add")
print s.isIsomorphic("foo", "bar")
print s.isIsomorphic("aa", "ab")