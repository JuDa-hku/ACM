from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        end, first, stateSet, checkSet, chDict = 0, 0, set(),set(), defaultdict(int)
        lengthRes = len(s)
        for ch in t:
            stateSet.add(ch)
            checkSet.add(ch)
            chDict[ch] += 1
        minimumLength = len(s)
        if len(s) == 0:
            return " "
        if s[0] in checkSet:
            chDict[s[0]] -= 1
            if chDict[s[0]] == 0:
                stateSet.remove(s[0])
            
        while end<=len(s)-1:
            if stateSet:
                end += 1
                if end == len(s):
                    break
                if s[end] in checkSet:
                    chDict[s[end]] -= 1
                    if s[end] in stateSet and chDict[s[end]]==0:
                        stateSet.remove(s[end])
                
            if not stateSet:
                if s[first] in checkSet:
                    if end-first<lengthRes:
                        lengthRes = end-first
                        res = [first, end]
                    chDict[s[first]] += 1
                    if chDict[s[first]] == 1:
                        stateSet.add(s[first])
                first += 1
#            print first, end, stateSet, chDict

        if lengthRes<len(s):
            return s[res[0]:res[1]+1]
        else:
            return ""
        
                    

S = "ADOBECODEBANCDEttt"
T = "ABC"
s = Solution()
print s.minWindow(S, T)
S = "a"
T = "aa"
print s.minWindow(S, T)
                
        