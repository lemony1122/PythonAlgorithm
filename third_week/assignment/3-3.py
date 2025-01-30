from collections import deque


def island_bfs(grid, start):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    visited = []
    count = 0
    rows = len(grid)
    columns = len(grid[0])

    for r in range(rows):
        for c in range(columns):
            if grid[r][c]!=1:
                continue
            count+=1
            remain = deque([r,c])

            while remain:
                x,y = deque.popleft()
                grid[x][y]="0"

                for i in range(4):
                    nx = x +dx
                    ny = y+dy
                    if nx <0 or nx >= rows or ny>=columns or ny<0 or grid[nx][ny] !='1':
                        continue
                    remain.append([nx,ny])



    return count



assert island_bfs(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_bfs(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3