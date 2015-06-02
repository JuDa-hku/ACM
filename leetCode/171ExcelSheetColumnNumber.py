class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dictNum = {}
        for num, alp in zip(range(1,27,1), alph):
            dictNum[alp] = num
        res = 0
        for i in xrange(len(s)):
            res = 26*res + dictNum[s[i]]
        return res
        
        
