# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorderIter = iter(postorder[::-1])
        valToidx = { val: idx for idx, val in enumerate(inorder) }

        def helper(start, end):
            if start > end:
                return None

            val = next(postorderIter)
            mid = valToidx[val]
            root = TreeNode(val)

            root.right = helper(mid + 1, end)
            root.left = helper(start, mid - 1)
            return root

        return helper(0, len(inorder) - 1)
