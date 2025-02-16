# 16/2/25
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/description/

from functools import reduce
def constructDistancedSequence(n: int) -> list[int]:
    valid_seq = []
    visited = [0 for _ in range(2 * n - 1)]

    def addLowerSequence(v: int, visited: list[int]):
        if v == 1:
            idx = visited.index(0)
            visited[idx] = 1

            valid_seq.append(visited)

            return

        for i in range(2 * n - 1):
            # Pair will exceed bounds
            if i + v >= 2 * n - 1:
                continue

            # Both indices aren't valid for v to be 'v' apart
            # from one another.
            if visited[i] or visited[i + v]:
                continue

            ### Optimisations:
            #   This needs to be replaced with backtracking. Otherwise, it is an
            #   O(n) operation applied for all O(n - 1)! iterations.
            visited_clone = [visited[i] for i in range(2 * n - 1)]
            visited_clone[i] = visited_clone[i + v] = v
            
            addLowerSequence(v - 1, visited_clone)
                
        return

    # The lexographically largest seq. will always start with 'n'. This
    # reduces the # of iterations by a factor of 'n'.
    visited[0] = visited[n] = n

    addLowerSequence(n - 1, visited)

    def lexicographicalList(l1: list, l2: list) -> list:
        assert len(l1) == len(l2)

        for v1, v2 in zip(l1, l2):
            if v1 == v2:
                continue

            return l1 if v1 > v2 else l2

        return l1

    return reduce(lexicographicalList, valid_seq)

### Optimisations
#   This solution HAS backtracking, however it prioritises the wrong heuristic. This
#   ensures that the first 'k' values of 'n' will be as high as possible. Instead,
#   it should ensure that the NEXT FILLED INDEX is as high as possible. It should
#   recurse via the next INDEX not the next 'n'.
def WithBacktracking(n: int) -> list[int]:
    visited = [0 for _ in range(2 * n - 1)]

    if n == 1:
        return [1]

    def addLowerSequence(v: int):
        if v == 1:
            idx = visited.index(0)
            visited[idx] = 1

            return True

        for i in range(2 * n - 1):
            # Pair will exceed bounds
            if i + v >= 2 * n - 1:
                continue

            # Both indices aren't valid for v to be 'v' apart
            # from one another.
            if visited[i] or visited[i + v]:
                continue

            visited[i] = visited[i + v] = v
            if addLowerSequence(v - 1):
                return True
            
            visited[i] = visited[i + v] = 0
   
        return False

    # The lexographically largest seq. will always start with 'n'. This
    # reduces the # of iterations by a factor of 'n'.
    visited[0] = visited[n] = n

    if addLowerSequence(n - 1):
        return visited
        

print(constructDistancedSequence(3))
print(constructDistancedSequence(5))
print(constructDistancedSequence(12))
