# 99. Recover Binary Search Tree
# https://leetcode.com/problems/recover-binary-search-tree/
# https://www.youtube.com/watch?v=wGXB9OWhPTg

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.firstWrong = self.secondWrong = None
        self.morrisTraverse(root)
        self.firstWrong.val, self.secondWrong.val = self.secondWrong.val, self.firstWrong.val

    
    def morrisTraverse(self, root):
        pre = temp = None

        def findPossibleErrors(prev, current):
            if prev and current.val < pre.val:
                if not self.firstWrong:
                    self.firstWrong = prev
                self.secondWrong = current

        def visitThenIterate(prev, current):
            findPossibleErrors(prev, current)
            prev, current = current, current.right

        while root:
            if not root.left:
                findPossibleErrors(pre, root)
                pre, root = root, root.right

            else:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right

                if temp.right is None:
                    temp.right = root
                    root = root.left
                else:
                    temp.right = None
                    findPossibleErrors(pre, root)
                    pre, root = root, root.right
