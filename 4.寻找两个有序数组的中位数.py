#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        left, right = (n + m + 1) // 2, (n + m + 2) // 2

        def getKth(nums1, start1, end1, nums2, start2, end2, k):
            len1 = end1 - start1 + 1
            len2 = end2 - start2 + 1

            if len1 > len2:
                return getKth(nums2, start2, end2, nums1, start1, end1, k)
            if len1 == 0:
                return nums2[start2 + k - 1]
            
            if k == 1:
                return min(nums1[start1], nums2[start2])
            
            i = start1 + min(len1, k // 2) - 1
            j = start2 + min(len2, k // 2) - 1

            if nums1[i] > nums2[j]:
                return getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
            else:
                return getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
            
        return (getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) * 0.5
# @lc code=end

