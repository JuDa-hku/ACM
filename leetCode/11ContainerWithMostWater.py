class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        maxV, leftIndex, rightIndex = 0, 0, 0
        left, right = 0, len(height)-1
        while left<right:
            volum = min(height[left], height[right])*(right-left)
            if volum > maxV:
                maxV = volum
                leftIndex, rightIndex = left+1, right+1
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
        return maxV

h=[14,0,12,3,8,3,13,5,14,8]        
s = Solution()
print s.maxArea(h)