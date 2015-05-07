class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        n = len(digits)
        digits[n-1] = digits[n-1] + 1
        if digits[n-1]<10:
            return digits
        for i in xrange(n-2, -1, -1):
            digits[i+1] = 0
            digits[i] += 1
            if digits[i] < 10:
                return digits
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
            return digits

s = Solution()
print s.plusOne([9,9,9,9,9])
print s.plusOne([8,9,9,9,9])
print s.plusOne([0])
print s.plusOne([9])
print s.plusOne([1,0,0])

            