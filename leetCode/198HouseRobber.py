class Solution:
    

    def rob(self, num):
        store = [0] * 1000
        return self.robHelp(num, store)

    def robHelp(self, num,  store):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        store[0] = num[0]
        store[1] = max(num[0], num[1])
        for i in range(2,len(num)):
            numWithi = store[i-2] + num[i]
            numWithouti = store[i-1]
            if numWithi>numWithouti:
                store[i] = numWithi
            else:
                store[i] = numWithouti
        return store[len(num)-1]


num = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,2]
s = Solution()
print s.rob(num)

num = [8]
print s.rob(num)

num = [2,4,6, 8]
print s.rob(num)