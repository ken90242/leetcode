# 331. Verify Preorder Serialization of a Binary Tree.py
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1 # 一開始的root
        for char in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if char.isdigit():
                slots += 2

        return slots == 0
