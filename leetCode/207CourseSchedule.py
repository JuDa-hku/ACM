from collections import defaultdict
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if len(prerequisites) == 0:
            return True
        G = defaultdict(list)
        for i in xrange(numCourses):
            G[i] = []
        for course in prerequisites:
            G[course[1]].append(course[0])
        count = dict((u,0) for u in G)
        for u in G:
            for v in G[u]:
                count[v] += 1
        Q = [u for u in G if count[u]==0]
        if len(Q) == 0:
            return False
        S = []
        while Q:
            u = Q.pop()
            S.append(u)
            for v in G[u]:
                count[v] -= 1
                if count[v] == 0:
                    Q.append(v)
        for u in G:
            if count[u] != 0:
                return False
        return True

        
s = Solution()
print s.canFinish(2, [[1,0]])



                
            









