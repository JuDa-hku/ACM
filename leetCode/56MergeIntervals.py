# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
from operator import attrgetter
class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals=sorted(intervals, key=attrgetter('start', 'end'), reverse=True)
        resIntervals = []
        while intervals:
            currInterval = intervals.pop()
            if not intervals:
                resIntervals.append(currInterval)
                return resIntervals
            else:
                nextInterval = intervals.pop()
                if nextInterval.start<=currInterval.end:
                    nextInterval.start = currInterval.start
                    nextInterval.end = max(nextInterval.end, currInterval.end)
                    intervals.append(nextInterval)
                else:
                    intervals.append(nextInterval)
                    resIntervals.append(currInterval)
        return resIntervals

                



a = Interval(1,3)
a1 = Interval(2,2.5)
a2 = Interval(2.5,10)
b = [a,a1,a2]
#b = []
s = Solution()
resIntervals = s.merge(b)
print [[a.start, a.end] for a in resIntervals]