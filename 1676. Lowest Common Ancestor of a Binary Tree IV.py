# 1676. Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.nodes = set([node.val for node in nodes])
        self.lca = None
        self.helper(root)
        return self.lca
    
    def helper(self, root):
        if not root:
            return 0
        
        count = self.helper(root.left) + self.helper(root.right)
        if root.val in self.nodes:
            count += 1

        if not self.lca and count == len(self.nodes):
            self.lca = root
        
        return count
