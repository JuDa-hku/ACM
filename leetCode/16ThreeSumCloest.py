class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumClosest(self, num, target):
        num.sort()
        minSum, distance = 0, float('inf')
        if len(num) <3:
            return []
        for start in xrange(len(num)-2):
            newTarget = target - num[start]
            middle = start + 1
            end = len(num)-1
            while end>middle:
                tmpDistance = abs(newTarget-num[end]-num[middle])
                distance = min(distance, tmpDistance)
                if distance == tmpDistance:
                    minSum = num[start] + num[middle] + num[end]
                if num[end] + num[middle] >newTarget:
                    end = end - 1
                elif num[end] + num[middle] <newTarget:
                    middle = middle +1
                elif num[end] + num[middle] == newTarget:
                    return target
        return minSum
        
                    
                
                
                
                
                

        return res1

s = Solution()
arr = [-1,2,1,-4,-2]
arr = [-10,-82,-70,92,39,-98,94,93,27,-74,1,-80,-95,-36,10,-12,43,92,-61,30,-26,100,-35,-54,-91,-58,-73,-66,86,8,1,49,-46,55,-89,39,45,66,96,42,80,-76,-69,53,-75,16,-13,53,-37,98,-59,72,41,-50,-23,-21,91,22,4,-80,1,-89,93,5,82,20,5,-77,95,16,-51,-21,0,-66,-84,-17,6,-65,12,94,-38,1,71,23,-71,50,8,28,80,-47,5,-13,69,-9,13,41,83,-61,-87,-51,89,-10,37,-73,-64,11,49]
print s.threeSumClosest(arr, 215)