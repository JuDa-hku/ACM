class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i, j = 0, 0
        tmp = [0]*(m+n)
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                tmp[i+j] = nums1[i]
                i += 1
            else:
                tmp[i+j] = nums2[j]
                j += 1
        if i<m:
            for k in range(i, m, 1):
                tmp[j+k] = nums1[k]
        if j<n:
            for k in range(j, n, 1):
                tmp[i+k] = nums2[k]
        nums1[::1] = tmp[::1]
        print tmp

nums1, nums2 = [0], [1]
s = Solution()
s.merge(nums1,0,nums2,1)