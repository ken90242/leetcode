# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection:

    def __init__(self):
        self.ele2idx = collections.defaultdict(set)
        self.ele = []
        

    def insert(self, val: int) -> bool:
        i = len(self.ele)
        self.ele2idx[val].add(i)
        self.ele.append(val)

        if len(self.ele2idx[val]) > 1:
            return True
        return False
        
        

    def remove(self, val: int) -> bool:
        if len(self.ele2idx[val]) == 0:
            return False

        lastIdx = len(self.ele) - 1
        lastVal = self.ele[lastIdx]
        valIdx = self.ele2idx[val].pop()
        self.ele[valIdx], self.ele[lastIdx] = self.ele[lastIdx], self.ele[valIdx]
        self.ele2idx[lastVal].add(valIdx)
        self.ele2idx[lastVal].remove(lastIdx)
        self.ele.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.ele)
