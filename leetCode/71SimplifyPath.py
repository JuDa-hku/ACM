class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        pathList = path.split('/')
#        print pathList
        stack = []
        for pa in pathList:
            if pa == '/' or pa == '.' or pa=='':
                continue
            elif pa == '..' and  stack:
                stack.pop()
            elif pa == '..' and not stack:
                continue
            else:
                stack.append(pa)
        if len(stack) == 0:
            return '/'
        else:
            return '/' + '/'.join(stack)


s = Solution()
path = '/home/'
print s.simplifyPath(path)
path = '/home//foo/'
print s.simplifyPath(path)
path = '/../'
print s.simplifyPath(path)
path = '/a/./b/../../c/'
print s.simplifyPath(path)
path = "/home/../../a/b"
print s.simplifyPath(path)
