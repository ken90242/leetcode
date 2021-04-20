# https://leetcode.com/problems/range-sum-query-mutable/
# 307. Range Sum Query - Mutable

class SegementNode:
    def __init__(self, start, end, val=0):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = val
    

class NumArray:
    def buildTree(self, start, end):
        if end < start:
            return None
        elif start == end:
            return SegementNode(start, end, self.nums[start])

        mid = (start + end) // 2
        root = SegementNode(start, end)
        root.left = self.buildTree(start, mid)
        root.right = self.buildTree(mid + 1, end)
        
        root.sum = root.left.sum + root.right.sum
        
        return root

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.buildTree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.updateNode(self.root, index, val)
    
    def updateNode(self, node, index, val):
        if node.start > index or node.end < index:
            return
        elif node.start == node.end == index:
            node.sum = val
        else:
            self.updateNode(node.left, index, val)
            self.updateNode(node.right, index, val)
            node.sum = node.left.sum + node.right.sum
        

    def sumRange(self, left: int, right: int) -> int:
        return self.query(self.root, left, right)
    
    def query(self, node, start, end):
        if node.start == start and node.end == end:
            return node.sum
        mid = (node.start + node.end) // 2
        if end <= mid:
            return self.query(node.left, start, end)
        elif start >= mid + 1:
            return self.query(node.right, start, end)
        else:
            return self.query(node.left, start, mid) + self.query(node.right, mid + 1, end)
