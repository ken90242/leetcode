# 315. Count of Smaller Numbers After Self
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        results = [0] * len(nums)
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums

            mid = len(nums) // 2
            leftSorted = mergeSort(nums[:mid])
            rightSorted = mergeSort(nums[mid:])
            m, n = len(leftSorted), len(rightSorted)

            i = j = 0
            while i < m or j < n:
                if j == n or (i < m and leftSorted[i][1] <= rightSorted[j][1]):
                    results[leftSorted[i][0]] += j
                    nums[i + j] = leftSorted[i]
                    i += 1
                else:
                    nums[i + j] = rightSorted[j]
                    j += 1
            
            return nums

        mergeSort(list(enumerate(nums)))
        
        return results
