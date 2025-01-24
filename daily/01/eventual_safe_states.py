# 24/1/25
# https://leetcode.com/problems/find-eventual-safe-states/description/

def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
    n = len(graph)

    visited = [False for _ in range(n)]
    safe_states = set(range(n))

    def DFS(src: int):
        visited[src] = True
        on_stack.add(src)

        for neighbour in graph[src]:
            # Removed nodes from safe_states eventually result in a cycle.
            if neighbour not in safe_states:
                return True
            
            # If the neighbour is already on the 'local' stack, there has
            # been a cycle.
            if neighbour in on_stack:
                return True
            
            if visited[neighbour]:
                continue

            # If a cycle is detected, backtrack!
            if DFS(neighbour):
                return True
        
        # NOTE: Typically you'd remove src from visited to allow further exploration. However,
        # As its neighbours have all passed the cycle test, we allow it to be in safe_states
        # and do not revisit.

        on_stack.remove(src)

        return False
    
    for (node, _) in enumerate(graph):
        if not visited[node]:
            on_stack = set()

            if DFS(node):
                safe_states -= on_stack

    # Leverages the fact that set's are returned in insertion-order to prevent sorting.
    return list(safe_states)

print(eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]))