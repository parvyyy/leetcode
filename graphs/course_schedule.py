# https://leetcode.com/problems/course-schedule/description/

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # Idea: Form a graph & run a DFS to check for a cycle.

    g = [[] for _ in range(numCourses)]
    for c1, c2 in prerequisites:
        g[c2].append(c1)

    def hasCycle(v: int) -> bool:
        visited[v] = on_stack[v] = True

        for neighbour in g[v]:
            if on_stack[neighbour]:
                return True
            
            if visited[neighbour]:
                continue
            
            if hasCycle(neighbour):
                return True
        
        # If it is backtracking, it is no longer part of the 'stack', allowing
        # further exploration by another vertex potentially.
        on_stack[v] = False

        return False

    # We do not create a new one each iteration, as it restores itself when backtracking!
    on_stack = [False for _ in range(numCourses)]
    visited = [False for _ in range(numCourses)]

    for course in range(numCourses):
        if visited[course]:
            continue

        if hasCycle(course):
            return False
        
    return True

print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))