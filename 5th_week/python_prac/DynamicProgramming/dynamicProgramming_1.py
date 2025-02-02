 # 피보나치 수열
 # 일반 계산
def fibo(n):
    if n in [1, 2]:  #if n==1 or 2
        return 1
    return fibo(n-1) + fibo(n-2)


assert fibo(10) == 55            # 시간이 너무 오래 걸림 (비효율적)
assert fibo(100) == 354224848179261915075

# DP로 풀어본 것
memo = {1: 1, 2: 1}


def fibo_dp(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return memo[n]


assert fibo_dp(10) == 55
assert fibo_dp(100) == 354224848179261915075