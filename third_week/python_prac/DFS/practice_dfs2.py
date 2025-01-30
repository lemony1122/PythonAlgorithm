
# 섬의 갯수 반환

def island_dfs_stack(grid,):
    count = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1':
                continue
            stack = [(r,c)]
            count += 1

            while stack:
                x,y = stack.pop()
                grid[x][y] = '0'

                for i in range(4):
                    nr = x + dx[i]
                    nc = y+ dy[i]
                    if nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!='1':
                        continue
                    stack.append((nr,nc))

    return count






def island_dfs_recursive(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    def dfs(r,c):
        grid[r][c]='0'
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != '1':
                continue
            dfs(nr,nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]!='1':
                continue
            count+=1
            dfs(r,c)
    return count







assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3

assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3