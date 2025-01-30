graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

def dfs_recursive(graph,start,visited):
    visited.append(start)

    for adj in graph[start]:
        if adj not in visited:
            dfs_recursive(graph,adj,visited)

    return visited


def dfs_stack(graph,start):
    visited = []
    stack= [start]

    while stack:
        next = stack.pop()
        visited.append(next)
        for adj in graph[next]:
            if adj not in visited:
                stack.append(adj)
    return visited



# 방법 1: 재귀함수
assert dfs_recursive(graph, 1, []) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 방법 2: 스택
assert dfs_stack(graph, 1) == [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]



