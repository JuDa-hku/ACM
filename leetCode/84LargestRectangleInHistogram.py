from collections import defaultdict
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        maxArea, indexStack = 0, []
        i = 0
        
        while i<len(height):
            print indexStack
            if not indexStack or height[i]>=height[indexStack[-1]]:
                indexStack.append(i)
                i += 1
            elif height[i]<height[indexStack[-1]]:
                hIndex = indexStack.pop()
                if not indexStack:
                    width = i
                if indexStack:
                    width = i-indexStack[-1]-1
                maxArea = max(maxArea, width*height[hIndex])

        while indexStack:
            hIndex = indexStack.pop()
            if not indexStack:
                width = len(height)
            if indexStack:
                width = len(height)-indexStack[-1]-1
            maxArea = max(maxArea, width*height[hIndex])
            
        return maxArea
            

        


s = Solution()
height = range(1,1000,1)
height = [5,5,1,7,1,1,5,2,7,6]
print s.largestRectangleArea(height)

