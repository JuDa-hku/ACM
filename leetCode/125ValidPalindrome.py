from collections import deque
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        s = s.strip(" ")
        deq = deque([])
        for ch in s:
            if 'a'<=ch<='z' or 'A'<=ch<='Z':
                deq.append(ch.lower())
            if '0'<=ch<='9':
                deq.append(ch)
        while deq:
            if len(deq) == 1:
                return True
            left = deq.popleft()
            right = deq.pop()
            if left != right:
                return False
        return True

    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        flag0, flag1 = False, False
        while start<end:

            if 'A'<=s[start]<='Z' or 'a'<=s[start]<='z':
                check0 = s[start].lower()
                flag0 = True
            elif '0'<=s[start]<='9':
                check0 = s[start]
                flag0 = True

            
            if 'A'<=s[end]<='Z' or 'a'<=s[end]<='z':
                check1 = s[end].lower()
                flag1 = True
            elif '0'<=s[end]<='9':
                check1 = s[end]
                flag1 = True
                
            if flag0 and flag1 and check0!=check1:
                return False
            elif flag0 and  flag1 and check0 == check1:
                start, end = start+1, end-1
            elif not flag0 and not flag1:
                start, end = start+1, end-1
            elif flag0 and not flag1:
                end = end-1
            elif not flag0 and flag1:
                start += 1
            flag0, flag1 = False, False
        return True
            

        
            
            
            

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("race a car")
print s.isPalindrome("1a  1")
print s.isPalindrome("1a  2")