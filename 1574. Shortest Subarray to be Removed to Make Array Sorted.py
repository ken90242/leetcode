# 1574. Shortest Subarray to be Removed to Make Array Sorted
# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while r > 0:
            if arr[r] < arr[r - 1]:
                break
            r -= 1
        
        if r == 0:
            return 0
        
        while l < len(arr) - 1:
            if arr[l] > arr[l + 1]:
                break
            l += 1
        
        toRm = min(len(arr) - l - 1, r)
        
        for iL in range(l + 1):
            if arr[iL] <= arr[r]:
                toRm = min(toRm, r - iL - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        
        return toRm
