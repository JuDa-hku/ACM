class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dictNum = {}
        for num, alp in zip(range(1,27,1), alph):
            dictNum[num] = alp
        res = ''
        while n>26:
            if n%26 == 0:
                res = res + 'Z'
                n = n/26-1
            else:
                res = res+dictNum[n%26]
                n = (n-n%26)/26
        if n == 0:
            return res[::-1]
        else:
            res = res+dictNum[n]
            return res[::-1]



s = Solution()
for i in xrange(1,53):
    print s.convertToTitle(i)