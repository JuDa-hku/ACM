class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):

        if x<0:
            return False
        if x < 10:
            return True
        high = 1
        while x/high >=10:
            high *= 10
        while x:
            left = x/high
            right = x%10
            print left, right, x
            if left != right:
                return False
            x = (x%high)/10
            high = high/100
        return True
        
s = Solution()
print s.isPalindrome(1000021)
print s.isPalindrome(123321)
