# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        times = collections.defaultdict(int)
        ans = 0

        def preorder(node, total):
            nonlocal ans
            if not node:
                return
            
            total += node.val
            
            if total == targetSum:
                ans += 1

            ans += times[total - targetSum]
            times[total] += 1
            
            preorder(node.left, total)
            preorder(node.right, total)
            
            times[total] -= 1
            
        preorder(root, 0)
        return ans
