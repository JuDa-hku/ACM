class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        C, maxLength = set(), 0
        front, back = 0, 0
        for i in s:
            back += 1
            if i not in C:
                C.add(i)
                continue
            else:
                maxLength = max(back-front-1, maxLength)
                while s[front] != i:
                    C.remove(s[front])
                    front += 1
                front += 1
        maxLength = max(maxLength, back-front)
        return maxLength
s= Solution()
print s.lengthOfLongestSubstring("abcabcbbabcd")
            
        