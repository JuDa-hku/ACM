class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s)==0 and len(p)==0:
            return True
        if len(s)==0 and len(p)!=0:
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True
        if len(s)!=0 and len(p)==0:
            return False
        if len(p)-p.count('*') > len(s):
            return False
        p = self.transform(p)
        res = [True] + [False for _ in range(len(s))]
        for i in p:
            if i != '*':
                for n in reversed(range(len(s))):
                    res[n+1] = res[n] and (i == s[n] or i=='?')
            else:
                for n in range(1, len(s)+1):
                    res[n] = res[n-1] or res[n]
            res[0] = res[0] and i == '*'
        return res[-1]
                    
    def transform(self, p):
        newp = [p[0]]
        for i in xrange(1,len(p),1):
            if p[i] == '*' and p[i-1]!='*':
                newp.append(p[i])
            if p[i] == '*' and p[i-1]=='*':
                continue
            if p[i] != '*':
                newp.append(p[i])
        return ''.join(newp)
                
            


s = Solution()
print s.isMatch("aa", "a")
print s.isMatch("aa","a") 
print s.isMatch("aa","aa")
print s.isMatch("aaa","aa")
print s.isMatch("aa", "*")
print s.isMatch("aa", "a*")
print s.isMatch("ab", "?*")
print s.isMatch("aab", "c*a*b")
print s.isMatch("", "")
print s.isMatch("", "****?")


z ="ababbbbbbaabbbbabaaabbaaaabaaababbbaababbaaabbaaaabbabaabbabbbbbabbaabbbaabbbbababbaabaaaabbabaaaabababbaababbbbaababbabaababbabbbbbaaaaababaabaaabaabbabaaaaabbaaaaabaaababbbbbbabbabbbbbababbaabaaaabbbbaa"

t = "*ba*a*b*****a*ba*a*****aa***bba**a**aab**aa*a****a*a*bb*aabb*bbb*aa*aba*bbbb**aba***a*ba**bba*****a**abb"

print s.transform(t)
z = "a"*32316
t = "a"*32317+""
print s.isMatch(z, t)



###this is the original code I wrote without optimize the dp matrix.

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if len(s)==0 and len(p)==0:
            return True
        if len(s)==0 and len(p)!=0:
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True
        if len(s)!=0 and len(p)==0:
            return False
        if len(p)-p.count('*') > len(s):
            return False
        p = self.transform(p)
        res = [[False for _ in range(len(p))] for _ in range(len(s))]
        if s[0] == p[0] or p[0] == '?' or p[0] == '*':
            res[0][0] = True
        for i in range(1,len(s),1):
            res[i][0] = (p[0] == '*')
        for i in range(1, len(p), 1):
            res[0][i] = (res[0][i-1] and p[i] == '*')
        for i in range(1, len(s), 1):
            for j in range(1, len(p), 1):
                if  p[j] != '?' and p[j] !='*':
                    res[i][j] = (res[i-1][j-1] and s[i] == p[j])
                if p[j] == '?':
                    res[i][j] = res[i-1][j-1]
                if p[j] == '*':
                    for t in range(i):
                        if res[t][j-1]:
                            res[i][j] = True
        return res[len(s)-1][len(p)-1]

    def transform(self, p):
        newp = [p[0]]
        for i in xrange(1,len(p),1):
            if p[i] == '*' and p[i-1]!='*':
                newp.append(p[i])
            if p[i] == '*' and p[i-1]=='*':
                continue
            if p[i] != '*':
                newp.append(p[i])
        return ''.join(newp)
                