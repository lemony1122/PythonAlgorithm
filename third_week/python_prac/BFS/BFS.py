from third_week.python_prac.BFS.BFS_structure import bfs_queue

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

assert bfs_queue(graph, 1) == [1, 2, 5, 9, 3, 6, 8, 10, 4, 7]