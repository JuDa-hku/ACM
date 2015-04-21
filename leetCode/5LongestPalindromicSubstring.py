class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
##consider the middle point of the substring
        middle = len(s)/2
        maxLength = 0
        for i in xrange(middle, 0, -1):
            if maxLength > 2*(i+1):
                break
                
            left, right = i-1, i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            
            left, right =i, i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            

            left, right =i-1, i
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            

        for i in xrange(middle, len(s), 1):
            if maxLength > 2*(len(s)-i):
                break
                
            left, right = i-1, i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            
            
            left, right =i, i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            

            left, right =i-1, i
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right += 1
            left,right = left+1, right-1
            length = right-left+1
            maxLength = max(maxLength, length)
            if maxLength == length:
                res = s[left:right+1]
            
        return  res
s = Solution()
print s.longestPalindrome('stringnirtsabcdefghijklmn')

    