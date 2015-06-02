# Definition for a point.
from __future__ import division
from collections import defaultdict

class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b
         
class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        n = len(points)
        res = defaultdict(int)
        samePoint = defaultdict(int)
        if n<= 2:
            return n
            
        for i in xrange(n):
            x1,y1 = points[i].x, points[i].y
            if samePoint[(x1, y1)] == 0:
                for j in xrange(i+1, n):
                    x2,y2 = points[j].x, points[j].y
                    if x1 == x2 and y1 == y2: 
                        samePoint[(x1, y1)] += 1
                    elif x1 == x2:
                        res[(x1,y1,x1)] += 1
                    else:
                        a, b = float(y1-y2)/(x1-x2), float(y1*x2-y2*x1)/(x2-x1)
                        res[(x1,y1,a,b)] += 1
                    
        maxim = 0
        if len(res) == 0:
            for key in samePoint:
                maxim = max(maxim, samePoint[key])
        else:
            for key in res:
                maxim = max(maxim, res[key]+samePoint[(key[0],key[1])])
        
        return maxim+1
            
a0, a1, a2 = Point(1,1),Point(1,1),Point(1,1)
s = Solution()
p = [a0,a1,a2]
print s.maxPoints(p)