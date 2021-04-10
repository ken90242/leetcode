# 1028. Recover a Tree From Preorder Traversal
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        read = 0
        i = 0
        while i < len(S) and S[i] != '-':
            read = read * 10 + int(S[i])
            i += 1
        root = TreeNode(read)
        stack = [root]

        while i < len(S):
            level = 0
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1

            read = 0
            while i < len(S) and S[i] != '-':
                read = read * 10 + int(S[i])
                i += 1
            
            node = TreeNode(read)

            if len(stack) > level:
                while len(stack) > level:
                    stack.pop()
                stack[-1].right = node
            else:
                stack[-1].left = node

            stack.append(node)

        return stack[0]
