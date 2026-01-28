from collections import deque, defaultdict
def BalanceTest(graph):
    """
    graph: dictionary of dictionaries
        graph[u][v] = +1 or -1 (edge sign)
    Returns: (is_balanced, group1, group2, conflict_cycle)
    """
    groups = {}

    for start in graph:
        if start in groups:
            continue  # already assigned
        groups[start] = 1
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v, sign in graph[u].items():
                if v not in groups:
                    # assign based on sign
                    groups[v] = groups[u] if sign > 0 else -groups[u]
                    queue.append(v)
                else:
                    # check consistency
                    if (sign > 0 and groups[v] != groups[u]) or (sign < 0 and groups[v] == groups[u]):
                        # Not balanced: find a cycle (for simplicity, just return conflicting edge)
                        return False, None, None, (u, v)

    # separate nodes into two groups
    group1 = [node for node, grp in groups.items() if grp == 1]
    group2 = [node for node, grp in groups.items() if grp == -1]
    return True, group1, group2, None

N1 = {
    1: {2: +1, 3: +1},
    2: {1: +1, 3: +1, 4: -1, 5: +1},
    3: {1: +1, 2: +1, 6: -1},

    4: {2: -1, 7: -1, 9: -1},
    5: {2: +1, 6: -1},
    6: {3: -1, 5: -1, 11: -1, 8: +1},

    7: {4: -1, 12: +1},
    8: {6: +1, 11: -1},
    9: {4: -1, 12: +1},

    10: {12: +1, 11: -1},
    11: {10: -1, 6: -1, 8: -1, 13: -1, 14: -1},

    12: {7: +1, 9: +1, 10: +1, 13: +1},
    13: {12: +1, 11: -1, 15: -1},

    14: {11: -1, 15: -1},
    15: {13: -1, 14: -1}
}

N2 = {
    1: {2: +1, 3: +1},
    2: {1: +1, 3: +1, 4: +1, 5: +1},
    3: {1: +1, 2: +1, 6: -1},

    4: {2: +1, 7: -1, 9: -1},
    5: {2: +1, 6: -1},
    6: {3: -1, 5: -1, 11: -1, 8: +1},

    7: {4: -1, 12: +1},
    8: {6: +1, 11: -1},
    9: {4: -1, 12: +1},

    10: {12: +1, 11: -1},
    11: {10: -1, 6: -1, 8: -1, 13: -1, 14: -1},

    12: {7: +1, 9: +1, 10: +1, 13: +1},
    13: {12: +1, 11: -1, 15: -1},

    14: {11: -1, 15: -1},
    15: {13: -1, 14: -1}
}
print(BalanceTest(N1))
print(BalanceTest(N2))