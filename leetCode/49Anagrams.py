class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        res, dictStr = [], {}
        for string in strs:
            tup = [i for i in string]
            tup.sort()
            if tuple(tup) in dictStr:
                dictStr[tuple(tup)] += 1
            else:
                dictStr[tuple(tup)] = 1
        for string in strs:
            tup = [i for i in string]
            tup.sort()
            if dictStr[tuple(tup)] > 1:
                res.append(string)
        return res
        
        


s = Solution()
strs = ["abc", "cba", "cb", "ab", "acb", "abc"]
print s.anagrams(strs)

        