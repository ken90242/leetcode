# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/

class Solution:
    def exist(self, level, target):
        root = self.root
        l, r = 0, 2 ** level - 1
        for _ in range(level):
            mid = (l + r) // 2
            if target <= mid:
                root = root.left
                r = mid
            else:
                root = root.right
                l = mid + 1
        return root is not None
            
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 0
        self.root = root
        while root.left:
            root = root.left
            level += 1

        l, r = 1, 2 ** level - 1

        while l <= r:
            mid = (l + r) // 2
            if self.exist(level, mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return 2 ** level - 1 + l
