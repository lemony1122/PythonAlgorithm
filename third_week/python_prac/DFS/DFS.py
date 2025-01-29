from third_week.python_prac.DFS.DFS_structure import *

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
# 방법 1: 재귀함수
assert dfs_recursive(graph, 1, []) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 방법 2: 스택
assert dfs_stack(graph, 1) == [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]