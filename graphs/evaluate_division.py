from typing import List
from collections import defaultdict, deque
import math

def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """ 
        Create a weighted, directed graph.

        Each edge gets the value (e.g. A --> B has a weight of 2, B --> A a weight of 1/2)

        To find A --> C, traverse through, but instead of the summation, it is the multiplication
        of weights when doing Dijikstra's
    """

    adj_list = defaultdict(list)

    for (v1, v2), val in zip(equations, values):
        adj_list[v1].append((v2, val))
        adj_list[v2].append((v1, 1 / val))
    
    division_res = []
    for src, dest in queries:
        if src not in adj_list or dest not in adj_list:
            division_res.append(-1.0)
            continue

        # Dijikstra's

        dist = { v: math.inf for v in adj_list.keys() }
        predecessor = { v: -1 for v in adj_list.keys() }
        v_set = set(adj_list.keys())

        dist[src] = 1

        while len(v_set) > 0:
            # Finds 'v' such that dist[v] is minimal. Takes O(V) time.
            # This can be optimised with the use of a priority queue (O(log(V)))
            v = min(v_set, key=lambda vertex: dist[vertex])
            v_set.remove(v)

            # O(d(v))
            for (neighbour, weight) in adj_list[v]:
                # Edge relaxation
                if dist[v] * weight < dist[neighbour]:
                    dist[neighbour] = dist[v] * weight
                    predecessor[neighbour] = v

        division_res.append(dist[dest])
        
    return division_res