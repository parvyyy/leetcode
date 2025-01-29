# https://leetcode.com/problems/course-schedule-ii/description

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # Run a topological sort. That is, sort the nodes by their indegree & perform a DFS
    # traversal, adding nodes on the path.

    g = [[] for _ in range(numCourses)]
    in_degree = [0 for _ in range(numCourses)]

    for c1, c2 in prerequisites:
        g[c2].append(c1)
        in_degree[c1] += 1

    def DFS(v: int):
        visited[v] = on_stack[v] = True

        for neighbour in g[v]:
            if on_stack[neighbour]:
                return True
            
            if visited[neighbour]:
                continue

            if DFS(neighbour):
                return True

        on_stack[v] = False
        ordering.append(v)

        return False

    visited = [False for _ in range(numCourses)]
    on_stack = [False for _ in range(numCourses)]

    ordering = []
    for (course, _) in sorted(enumerate(in_degree), key=lambda x: x[1]):
        if visited[course]:
            continue

        if DFS(course):
            return []

    return ordering[::-1]

print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(1, []))
print(findOrder(2, [[1,0]]))
print(findOrder(2, [[0,1],[1,0]]))