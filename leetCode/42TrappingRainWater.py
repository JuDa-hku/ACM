class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        start, end, res = 0,0,0
        if len(height) <=2:
            return 0
        while end!=len(height)-1:
            if height[start] == 0 or height[start+1]>=height[start]:
                start += 1
                end = start
            elif height[end]<=height[start]:
                end += 1
            elif height[end]>height[start]:
#                print 'volum',self.calculate(height, start, end)
                res += self.calculate(height, start, end)
                start = end
        if end == len(height)-1 and height[end]<height[start]:
            res += self.calculate1(height, start, end)
        if end == len(height)-1 and height[end]>=height[start]:
            res += self.calculate(height, start, end)
        return res

    def calculate1(self, height, start, end):
        stack = height[start:end+1]
        end = stack.pop()
        res = 0
        while stack:
            start = stack.pop()
            if start>=end:
                end = start
            if start<end:
                res = res + end - start
        return res

    def calculate(self,height, start, end):
        h = height[start:end+1]
        if len(h)<=2:
            return 0
        minmum = min(height[start], height[end])
        totalVal = (len(h)-2)*minmum
        for num in h[1:len(h)-1]:
            if num>minmum:
                totalVal -= minmum
            else:
                totalVal -= num
        return totalVal


s = Solution()
nums =[0,1,0,2,1,0,1,3,2,1,2,1]
nums =range(10,0,-1)
nums.append(3)
nums = [4,2,0,3,2,5]
print s.trap(nums)

##a revised nicer solution should be "check two side and count the total number of volumn we can have in the map and then minus then volumn of rocks", when the leftbar is smaller we move to the right and vice versa.