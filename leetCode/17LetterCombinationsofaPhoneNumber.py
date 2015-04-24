class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterHelp(self, letter, digits, digToLetDict, resSet):
        if digits == '':
            resSet.add(letter)
            return
        else:
            for s in digToLetDict[digits[0]]:
                self.letterHelp(letter+s, digits[1:], digToLetDict, resSet)
        return resSet
        
        
    def letterCombinations(self, digits):
        letter,  resSet = '', set()
        digToLetDict = {'2':'abc', '3':'def','4':'ghi','5':'jkl'
                        ,'6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        #print digToLetDict
        if len(digits) == 0:
            return []
        resSet = self.letterHelp(letter, digits, digToLetDict, resSet)
        return list(resSet)

s = Solution()
print s.letterCombinations("23")
        