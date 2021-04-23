# 327. Count of Range Sum
# https://leetcode.com/problems/count-of-range-sum/

class BIT:
    def __init__(self, size):
        self.table = [0] * (size + 1)
    
    def update(self, i, val):
        while i < len(self.table):
            self.table[i] += val
            i += (i & -i)
    
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.table[i]
            i -= (i & -i)

        return ret

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sums = [0]
        for val in nums:
            sums.append(val + sums[-1])
        
        sSums = sorted(sums)

        bit = BIT(len(sums))

        count = 0
        for val in sums:
            l = self.lowerBound(val - upper, sSums)
            r = self.upperBound(val - lower, sSums)
            
            if l != -1 and r != -1:
                count += bit.query(r + 1) - bit.query(l)

            bit.update(1 + self.lowerBound(val, sSums), 1)

        return count
    
    def lowerBound(self, val, nums):
        l, r = 0, len(nums) - 1
        idx = -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < val:
                l = mid + 1
            elif nums[mid] > val:
                r = mid - 1
            else:
                idx = mid
                r = mid - 1
        
        return l if idx == -1 else idx
            
        
    def upperBound(self, val, nums):
        l, r = 0, len(nums) - 1
        idx = -1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < val:
                l = mid + 1
            elif nums[mid] > val:
                r = mid - 1
            else:
                idx = mid
                l = mid + 1
        
        return r if idx == -1 else idx        
