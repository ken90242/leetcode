# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/submissions/

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        stack = [(root, [root.val], root.val)]
        ans = []
        
        while stack:
            node, path, total = stack.pop()
            if node.left:
                stack.append((node.left, path + [node.left.val], total + node.left.val))
            
            if node.right:
                stack.append((node.right, path + [node.right.val], total + node.right.val))
                
            if not node.left and not node.right and total == targetSum:
                ans.append(path)
        
        return ans
