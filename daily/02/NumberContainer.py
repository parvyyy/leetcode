# 8/1/25
# https://leetcode.com/problems/design-a-number-container-system/description/

from collections import defaultdict
import heapq
class NumberContainer:
    def __init__(self):
        self.container = defaultdict(list)
        self.idx_to_n = defaultdict(lambda: -1)

    # Lazily Updates
    def change(self, index: int, number: int) -> None:
        self.idx_to_n[index] = number

        heapq.heappush(self.container[number], index)

    def find(self, number: int) -> int:
        adj_idxs = self.container[number]

        if len(adj_idxs) == 0:
            return -1
        
        # Go through the 'adjacent' indices until it finds
        # the smallest, non-stale value.
        while adj_idxs:
            idx = adj_idxs[0]

            # Validates that the index is not a 'stale',
            # and already changed.
            if self.idx_to_n[idx] == number:
                return idx
            
            # Otherwise, remove the stale index
            heapq.heappop(adj_idxs)

        return -1

n = NumberContainer()
n.find(10)
n.change(2, 10)
n.change(1, 10)
n.change(3, 10)
n.change(5, 10)
n.find(10)
n.change(1, 20)
n.find(10)