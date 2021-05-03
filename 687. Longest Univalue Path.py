# 687. Longest Univalue Path
# https://leetcode.com/problems/longest-univalue-path/

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0
        def getLen(node):
            nonlocal ans
            if not node:
                return 0
            
            leftLen = getLen(node.left)
            rightLen = getLen(node.right)
            
            
            right = left = 0
            if node.left and node.left.val == node.val:
                left = leftLen + 1
            
            if node.right and node.right.val == node.val:
                right = rightLen + 1
            
            ans = max(ans, left + right)
            return max(left, right)
        
        getLen(root)

        return ans
