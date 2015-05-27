from collections import deque
class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
#calculate how much you can get at i+1 if you start at gas station i
        n = len(gas)
        get = [0]*n
        for i in xrange(n):
            get[i] = gas[i]-cost[i]
        if n == 1 and get[0]>=0:
            return 0
        if n == 1 and get[0]<0:
            return -1
        checkedSet = set()
        path = deque([0])
        leftPath = deque(range(1,n,1))
        sumCal = get[0]
        while True:
            while sumCal<0:
                bi = path.popleft()
                if bi in checkedSet:
                    return -1
                if bi not in checkedSet:
                    checkedSet.add(bi)
                leftPath.append(bi)
                sumCal -= get[bi]
            ei = leftPath.popleft()
            sumCal += get[ei]
            path.append(ei)
            if sumCal>=0 and  not leftPath:
                return path[0]
      


s = Solution()
gas = [1,2]
cost = [2,1]
print s.canCompleteCircuit(gas, cost)
