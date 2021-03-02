# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        stack = []
        while stack or root:
            if root.val > p.val and root.val > q.val:
                stack.append(root.left)
            elif root.val < p.val and root.val < q.val:
                stack.append(root.right)
            else:
                break
            
            root = stack.pop()
        
        return root
