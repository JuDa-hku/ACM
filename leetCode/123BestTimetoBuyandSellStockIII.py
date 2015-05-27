class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        return self.maxProfitHelp(2, prices)


    def maxProfitHelp(self, k, prices):
#earnings to store how much you can earn in each increasing period
        earnings = []
        if len(prices)<2:
            return 0
        for start, end in zip(prices[:-1],prices[1:]):
            earnings.append(end-start)
        ##remove the first negavtive and last negative value
        while earnings[0] <= 0:
            earnings.pop(0)
            if earnings == []:
                return 0
        while earnings[-1] <= 0:
            earnings.pop()
        ##combine nearby negative and positive value
        tmpEarning = []
        posSum, negSum = 0,0
        for v in earnings:
            if v<0:
                negSum += v
                tmpEarning.append(posSum)
                posSum = 0
            if v>0:
                posSum += v
                tmpEarning.append(negSum)
                negSum = 0
        if earnings[-1]>0:
            tmpEarning.append(posSum)
        if earnings[-1]<0:
            tmpEarning.append(negSum)
        newEarning = []
        for v in tmpEarning:
            if v !=0 :
                newEarning.append(v)
        if k>len(newEarning):
            return sum([value for value in newEarning if value>0])
        global_max, local_max = [0]*(k+1), [0]*(k+1)
        for val in newEarning:
            for j in range(k,0,-1):
                local_max[j] = max(global_max[j-1]+max(val,0), local_max[j]+val)
                global_max[j] = max(local_max[j], global_max[j])
        return global_max[k]
