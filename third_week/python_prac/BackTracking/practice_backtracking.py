def nqueen(n):
    answer = []
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    # 1행 3열 이라면  case[1] = 3
    checked = [-1] * n

    def dfs(r):
        if r>=n:
            result =[["."]*n for _ in range(n)]
            for x in range(n):
                result[x][checked[x]] = 'Q'
            answer.append([''.join(result[idx]) for idx in range(n)])


        def is_ok(r):
            for i in range(r):
                if checked[i] == checked[r] or abs(i-r)==abs(checked[i]-checked[r]):
                    return False
            return True

        for c in range(n):
            checked[r]=c
            if is_ok(r):
                dfs(r+1)


    dfs(0)

    #백트래킹 기법




    return answer








assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]