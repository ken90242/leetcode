# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
	val2idx = { num: i for i, num in enumerate(inorder) }
	preorder = iter(preorder)
	
	def helper(inStart, inEnd):
		if inStart > inEnd:
			return None
		val = next(preorder)
		root = TreeNode(val)
		mid = val2idx[val]
		root.left = helper(inStart, mid - 1)
		root.right = helper(mid + 1, inEnd)
		return root

	return helper(0, len(inorder) - 1)
