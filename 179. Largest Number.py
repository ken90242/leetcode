# 179. Largest Number
# https://leetcode.com/problems/largest-number/

class LargerNum(str):

	def __lt__(x, y):
		return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans = ''.join(sorted(map(str, nums), key=LargerNum))
        if ans.startswith('0'):
            return '0'
        return ans
