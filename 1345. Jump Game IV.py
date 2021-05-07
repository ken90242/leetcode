# 1345. Jump Game IV
# https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        mapped = defaultdict(list)
        for i, num in enumerate(arr):
            mapped[num].append(i)
        
        visited = set([0])
        
        def getNext(i):
            ret = []
            for j in mapped[arr[i]]:
                if j != i and j not in visited:
                    ret.append(j)
            
            mapped.pop(arr[i])
            
            if i + 1 <= len(arr) - 1 and i + 1 not in visited:
                ret.append(i + 1)
            
            if i - 1 >= 0 and i - 1 not in visited:
                ret.append(i - 1)
            
            return ret

        jumps = [float('inf')] * len(arr)
        jumps[0] = 0
        
        queue = collections.deque([0])
        while queue:
            i = queue.popleft()
            for k in getNext(i):
                visited.add(k)
                jumps[k] = jumps[i] + 1
                if k == len(arr) - 1:
                    return jumps[-1]

                queue.append(k)
            
        return jumps[-1]
