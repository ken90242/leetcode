# 971. Flip Binary Tree To Match Preorder Traversal
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        flipped = []
        self.i = 0
        self.fail = False

        def dfs(root):
            if root:
                expect = voyage[self.i]
                self.i += 1

                if root.val != expect:
                    self.fail = True
                    return

                if self.i < len(voyage) and root.left and root.left.val != voyage[self.i]:
                    flipped.append(root.val)
                    dfs(root.right)
                    dfs(root.left)
                else:
                    dfs(root.left)
                    dfs(root.right)
        
        dfs(root)

        if self.fail:
            return [-1]
        return flipped
