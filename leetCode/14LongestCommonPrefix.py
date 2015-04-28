class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        minumLength, minumStr = float('inf'), ''
        for string in strs:
            if len(string) <minumLength:
                minumLength, minumStr = len(string), string
        return self.findPrefix(minumStr, 0, len(minumStr), strs)


    def findPrefix(self, string, start, end, strs):
        mid = (start+end)/2
        tmp = self.checkString(string[:mid], strs)
        if tmp and mid == len(string):
            return string[:mid]
        if tmp and not self.checkString(string[:mid+1], strs):
            return string[:mid]
        if tmp and self.checkString(string[:mid+1], strs):
            return self.findPrefix(string, mid+1, end, strs)
        if not tmp:
            self.findPrefix(string, start, mid, strs)
        return ""

        

    def checkString(self, stringChecked, strs):
        n = len(stringChecked)
        for string in strs:
            if string[:n] != stringChecked:
                return False
        return True
        
            
s = Solution()
print s.longestCommonPrefix(['foos', 'foolish', 'foosdanogn', 'foodmakg'])
print s.longestCommonPrefix(['aca', 'cba'])