# 333. Largest BST Subtree
# https://leetcode.com/problems/largest-bst-subtree/

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        MIN, MAX = float('-inf'), float('inf')
        def dfs(node):
            if not node:
                return MAX, MIN, 0
            
            lMin, lMax, lNum = dfs(node.left)
            rMin, rMax, rNum = dfs(node.right)
            # print(node.val, lMax, rMin)
            if lMax < node.val < rMin:
                return min(lMin, node.val), max(rMax, node.val), lNum + rNum + 1
            else:
                # when we return this, it is impossible for anybody to fit in
                return MIN, MAX, max(lNum, rNum)
        
        return dfs(root)[2]
