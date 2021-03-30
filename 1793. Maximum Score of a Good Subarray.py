# 1793. Maximum Score of a Good Subarray
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = j = k
        minimum = answer = nums[k]
        
        while 0 < i or j < len(nums) - 1:
            if (nums[i - 1] if i > 0 else 0) < nums[j + 1] if j < len(nums) - 1 else 0:
                j += 1
            else:
                i -= 1

            minimum = min(minimum, nums[i], nums[j])
            answer = max(answer, (j - i + 1) * minimum)
        
        return answer
