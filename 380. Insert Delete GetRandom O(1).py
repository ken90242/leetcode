# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:
    def __init__(self):
        self.ele2idx = {}
        self.ele = []

    def insert(self, val: int) -> bool:
        if val not in self.ele2idx:
            self.ele2idx[val] = len(self.ele)
            self.ele.append(val)
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.ele2idx:
            rmI = self.ele2idx[val]
            lastVal = self.ele[-1]
            # swap idxs
            self.ele[rmI], self.ele[-1] = self.ele[-1], self.ele[rmI]
            self.ele2idx[lastVal] = rmI
            
            # delete lastelement
            self.ele.pop()
            # delete ele2idx's val
            self.ele2idx.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.ele)
