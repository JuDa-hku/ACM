class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        cache = set()
        cache.add(n)
        nextN = n
        while True:
            nextN = self.cal(nextN)
            if nextN==1:
                return True
            elif nextN in cache:
                return False
            else:
                cache.add(nextN)

    def cal(self, n):
        res = 0
        while n>0:
            res = res + (n%10)**2
            n = n/10
        return res
    