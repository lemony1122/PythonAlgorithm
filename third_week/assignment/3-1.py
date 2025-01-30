from collections import deque

n, m = 5, 6
maze = [
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1]
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]

print(bfs(0, 0))
