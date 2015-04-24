class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findKth(self, nums1, nums2, k):
        if len(nums2) > len(nums1):
            nums1 , nums2 = nums2, nums1
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        nums2Cut = k/2-1
        if len(nums2)<k/2:
            nums2Cut = len(nums2)-1
        print nums2Cut, k, len(nums2), len(nums1)
        nums1Cut = k-nums2Cut-2
        if nums1[nums1Cut]>nums2[nums2Cut]:
            return self.findKth(nums1, nums2[nums2Cut+1:], k-nums2Cut-1)
        if nums1[nums1Cut]==nums2[nums2Cut]:
            return nums1[nums1Cut]
        else:
            return self.findKth(nums1[nums1Cut+1:], nums2, k-nums1Cut-1)


    def findMedianSortedArrays(self, nums1, nums2):        
        m, n = len(nums1), len(nums2)
        if (m+n)%2 == 1:
            return self.findKth(nums1, nums2, (m+n+1)/2)
        else:
            return float(self.findKth(nums1, nums2, (m+n)/2) + self.findKth(nums1, nums2, (m+n)/2+1))/2

        
s = Solution()
nums1 = range(100)
nums2 = range(200)
result = []
for k in xrange(1, 301, 1):
    result.append(s.findKth(nums1, nums2, k))
print s.findMedianSortedArrays(nums1, nums2)




##this is the original version.
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findKth(self, nums1, nums2, k):
        if len(nums2) > len(nums1):
            nums1 , nums2 = nums2, nums1
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        if len(nums1)>=k/2 and len(nums2)>=k/2 and nums1[k/2-1]>=nums2[k/2-1]:
            return self.findKth(nums1, nums2[k/2:], k-k/2)
        if len(nums1)>=k/2 and len(nums2)>=k/2 and nums1[k/2-1]<nums2[k/2-1]:
            return self.findKth(nums1[k/2:], nums2, k-k/2)
        if len(nums2) <k/2 and nums1[k/2-1]>=nums2[-1]:
            return self.findKth(nums1, [], k-len(nums2))
        if len(nums2) <k/2 and nums1[k/2-1]<nums2[-1]:
            return self.findKth(nums1[k/2:], nums2, k-k/2)

    def findMedianSortedArrays(self, nums1, nums2):        
        m, n = len(nums1), len(nums2)
        if (m+n)%2 == 1:
            return self.findKth(nums1, nums2, (m+n+1)/2)
        else:
            return float(self.findKth(nums1, nums2, (m+n)/2) + self.findKth(nums1, nums2, (m+n)/2+1))/2