class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
#it relates to the gap between m and n
        if m == n:
            return m
        gap, zero = n-m, 0
        for i in range(32):
            if 2**i>gap:
                zero = i-1
                break
            elif 2**i == gap:
                zero = i
                break
        tmpRes = '1'*(32-zero+1)+'0'*(zero+1)
        return int(tmpRes,2) & m & n

s = Solution()
print s.rangeBitwiseAnd(4,7)