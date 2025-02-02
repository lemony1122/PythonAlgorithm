import heapq


def dijkstra(graph, start):
    INF = 1e9
    result = [INF]*len(graph)
    result[start] = 0

    q = []
    heapq.heappush(q, (0,1))  # 기본적으로 최소힙 (누적비용, 노드 번호) 0번째 인덱스 값으로 최소힙

    while q:
        acc, node = heapq.heappop(q)

        if acc > result[node]:
            continue

        result[node] = acc
        for adj, cost in graph[node] :
            new_cost = acc + cost
            if new_cost < result[adj]:
                result[adj] = new_cost
                heapq.heappush(q,(new_cost,adj))

    return result
