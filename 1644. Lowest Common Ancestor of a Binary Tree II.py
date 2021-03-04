# 1644. Lowest Common Ancestor of a Binary Tree II
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}

        queue = [root]
        while queue:
            newQueue = []
            for node in queue:
                if node.left:
                    parents[node.left] = node
                    newQueue.append(node.left)
                if node.right:
                    parents[node.right] = node
                    newQueue.append(node.right)
            queue = newQueue
        
        if p not in parents or q not in parents:
            return None
        
        pAncestors = set()
        while p in parents:
            pAncestors.add(p)
            p = parents[p]
        
        while q in parents:
            if q in pAncestors:
                break
            q = parents[q]
        
        return q
