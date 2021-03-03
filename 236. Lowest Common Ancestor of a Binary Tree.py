# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        
        queue = [root]
        while queue:
            newQueue = []
            for node in queue:
                if node.left:
                    parent[node.left] = node
                    newQueue.append(node.left)

                if node.right:
                    parent[node.right] = node
                    newQueue.append(node.right)
            queue = newQueue

        pAncestors = set()

        while p in parent:
            pAncestors.add(p)
            p = parent[p]
        
        while q in parent:
            if q in pAncestors:
                break
            q = parent[q]

        return q
        