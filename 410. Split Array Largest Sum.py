# 410. Split Array Largest Sum
# https://leetcode.com/problems/split-array-largest-sum/submissions/

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:    
        def canSplit(bar):
            partNum = partSum = 0
            for num in nums:
                if num > bar:
                    return False

                if partSum + num > bar:
                    partSum = num
                    partNum += 1
                else:
                    partSum += num

            partNum += 1 # for the remaining partSum <- at least one number

            return partNum <= m

        l = 0
        r = 10 ** 8
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
