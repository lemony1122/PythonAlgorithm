import heapq


# 수업 예제 문제
# def delay_time(arr, n, k):
#     graph = {}
#
#     for u, v, w in arr:
#         if u not in graph:
#             graph[u] = []
#         graph[u].append((v, w))
#
#     Q = [(0, k)]
#     dist = {}
#
#     while Q:
#         time, node = heapq.heappop(Q)
#         if node not in dist:
#             dist[node] = time
#             if node in graph:
#                 for v, w in graph[node]:
#                     alt = time + w
#                     heapq.heappush(Q, (alt, v))
#
#     if len(dist) == n:
#         return max(dist.values())
#
#     return -1

def delay_time(arr, n, k):
#     그래프 표현
    graph = {}
    for start, end, time in arr:
        if start not in graph:
            graph[start] = []
        graph[start].append((end,time))

    q = [(0,k)]
    dist = {}

    while q:
        acc, cur = heapq.heappop((q))
        if cur not in dist:
            dist[cur] = acc
            if cur in graph:
                for adj, t in graph[cur]:
                    heapq.heappush(q,(acc+t, adj))

    if len(dist) == n:
           return max(dist.values())

    return -1



















assert delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert delay_time([[1,2,1]], 2, 1) == 1
assert delay_time([[1,2,1]], 2, 2) == -1