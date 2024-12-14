import time

def f(n):                   # 피보나치 수열 메모이제이션
    if memo[n] != -1:       # 이미 계산해서 메모에 있는 경우 그대로 반환 (O(1))
        return memo[n]
    elif n < 2:             # 점화식
        memo[n] = n
        return n
    else:                   # 아직 계산되지 않은 경우 계산해서 메모에 작성하고 반환
        memo[n] = f(n-1) + f(n-2)
        return memo[n]

def f_notmemo(n):           # 깡 재귀 방법 피보나치 수열
    return n if n < 2 else f_notmemo(n-1) + f_notmemo(n-2)

def f_bottomup(n):          # 바텀업
    dp = [0] * (n + 1)
    dp[1] = 1               # 점화식
    for i in range(2, n + 1):   # n = 2 부터 n이 커지는 방향으로 차근차근 계산
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input())
memo = [-1 for _ in range(n + 1)]

start = time.time()
print(f(n))
stop = time.time() - start
print('메모이제이션:', int(stop), '초 (', int(stop * 1000000), '나노초 )')

start = time.time()
print(f_notmemo(n))
stop = time.time() - start
print('재귀 피보나치:', int(stop), '초 (', int(stop * 1000000), '나노초 )')

start = time.time()
print(f_bottomup(n))
stop = time.time() - start
print('바텀업 피보나치:', int(stop), '초 (', int(stop * 1000000) ,'나노초 )')