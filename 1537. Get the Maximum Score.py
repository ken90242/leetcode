# 1537. Get the Maximum Score.py
# https://leetcode.com/problems/get-the-maximum-score/

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        ans = path1 = path2 = 0
        m, n = len(nums1), len(nums2)
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                path1 += nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                path2 += nums2[j]
                j += 1
            else:
                ans += max(path1, path2) + nums1[i]
                path1 = path2 = 0
                i += 1
                j += 1

        while i < m:
            path1 += nums1[i]
            i += 1
        
        while j < n:
            path2 += nums2[j]
            j += 1

        return (ans + max(path1, path2)) % (10 ** 9 + 7)
