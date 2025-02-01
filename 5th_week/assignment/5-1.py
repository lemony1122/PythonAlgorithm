# 죄송합니다... 너무 어려워서 답안 이해하면서 쳤습니다.



import heapq

def dijkstra(graph, start, end):
    #
    distances = {node: float('infinity') for node in range(1, len(graph) + 1)}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances[end]

graph = {
  1: {2: 4, 3: 2},
  2: {1:4, 3:5, 4:1},
  3: {1:2, 2:5, 4:7},
  4: {2:1, 3:7}
}

A, B = 1, 4
print(dijkstra(graph, A, B))