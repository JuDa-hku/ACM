# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

import copy
class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        insertIndex = self.findIndex(intervals, newInterval)
        print insertIndex
        if insertIndex == len(intervals):
            res = copy.deepcopy(intervals)
            if newInterval.start<=res[-1].end:
                res[-1].end = max(newInterval.end, res[-1].end)
            else:
                res.append(newInterval)
            return res
            
        res = []

        for i in xrange(len(intervals)):
            if i<insertIndex:
                res.append(intervals[i])
            if i==insertIndex:
                if not res:
                    res.append(newInterval)
                elif res:
                    if newInterval.start<=res[-1].end:
                        res[-1].end = max(newInterval.end, res[-1].end)
                    else:
                        res.append(newInterval)
                if intervals[i].start<=res[-1].end:
                    res[-1].end = max(intervals[i].end, res[-1].end)
                else:
                    res.append(intervals[i])
            if i>insertIndex:
                if intervals[i].start<=res[-1].end:
                    res[-1].end = max(intervals[i].end, res[-1].end)
                else:
                    res.append(intervals[i])
        return res

    def findIndex(self, intervals, newInterval):
        middle = len(intervals)/2
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1 and intervals[0].start<newInterval.start:
            return 1
        if len(intervals) == 1 and intervals[0].start>=newInterval.start:
            return 0
        if intervals[middle].start < newInterval.start:
            return middle +1 + self.findIndex(intervals[middle+1:], newInterval)
        if intervals[middle].start == newInterval.start:
            return middle + 1
        else:
            return self.findIndex(intervals[:middle], newInterval)

a1 = Interval(0,1)
a2 = Interval(5,5)
a3 = Interval(6,7)
a4 = Interval(9,11)
b = Interval(12,21)
s = Solution()
print [[i.start,i.end] for i in s.insert([a1,a2,a3,a4],b)]

            
            
                