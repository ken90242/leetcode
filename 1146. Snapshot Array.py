# 1146. Snapshot Array
# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snaps = self.arr[index]
        l, r = 0, len(snaps) - 1
        while l <= r:
            mid = (l + r) // 2

            if snaps[mid][0] == snap_id:
                l = mid + 1
            elif snaps[mid][0] < snap_id:
                l = mid + 1
            else:
                r = mid - 1

        return self.arr[index][l - 1][1]
