# 1740. Find Distance in a Binary Tree
# https://leetcode.com/problems/find-distance-in-a-binary-tree/

class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self.dfs(root, p, q)
        return self.dist(lca, p) + self.dist(lca, q)
        
    
    def dfs(self, node, p, q):
        if not node or node.val == p or node.val == q:
            return node

        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)

        if left and right:
            return node
        else:
            return left or right
    
    def dist(self, root, value):
        if root:
            if root.val == value:
                return 0
            return 1 + min(self.dist(root.left, value), self.dist(root.right, value))

        return float('inf')

        
