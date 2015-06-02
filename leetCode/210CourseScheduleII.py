class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        courseDict, countDict = {}, {}
        for i in xrange(numCourses):
            countDict[i] = 0
            courseDict[i] = []
        for prequest in prerequisites:
            courseDict[prequest[1]].append(prequest[0])
        for u in courseDict:
            for v in courseDict[u]:
                countDict[v] += 1

        Q, S = [], []
        for course in countDict:
            if countDict[course] == 0:
                Q.append(course)

        while Q:
            preCourse = Q.pop()
            S.append(preCourse)
            for v in courseDict[preCourse]:
                countDict[v] -= 1
                if countDict[v] == 0:
                    Q.append(v)

        for key in countDict:
            if countDict[key] != 0:
                return []

        return S


s = Solution()
print s.findOrder(4, [[1,0],[2,0],[3,1],[3,2],[1,2]])
            