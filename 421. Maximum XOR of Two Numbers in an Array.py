# 421. Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum = bitmask = 0

        for i in range(31, -1, -1):
            bitmask = bitmask | (1 << i)
            prefixes = set([num & bitmask for num in nums])
            
            possibleMaximum = maximum | (1 << i)
            for prefix in prefixes:
                # a ^ b = c, meaning a ^ c = b
                if (possibleMaximum ^ prefix) in prefixes:
                    maximum = possibleMaximum
                    break
            
        
        return maximum
