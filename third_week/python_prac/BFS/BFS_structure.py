from collections import deque

def bfs_queue(graph, start):
    visited = [start]    # 방문한 곳
    q = deque([start])   # 방문할 곳

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited