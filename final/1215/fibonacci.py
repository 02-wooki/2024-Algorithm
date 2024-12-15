# 피보나치 수열
import time


# 단순 재귀 구현
def f(n):
    if n < 2:
        return n
    else:
        return f(n - 1) + f(n - 2)

# 메모이제이션 (딕셔너리)
def g(n):
    global dmemo
    if n in dmemo:
        return dmemo[n]
    if n < 2:
        dmemo[n] = n
    else:
        dmemo[n] = g(n - 1) + g(n - 2)
    return dmemo[n]

# 메모이제이션 (리스트)
def h(n):
    global lmemo
    if lmemo[n] != -1:
        return lmemo[n]

    if n < 2:
        lmemo[n] = n
    else:
        lmemo[n] = h(n - 1) + h(n - 2)
    return lmemo[n]

def b(n):
    dp = [-1 for _ in range(n + 1)]
    for i in range(n + 1):
        if i < 2:
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + dp[i - 2]
    print(dp)
    return dp[n]

n = 35
print(n)
start = time.time()
print(f(n))
end = time.time() - start
print(f'재귀: {int(end)}초 ({int(end * 1000000)}나노초) 소요\n')

dmemo = {}
lmemo = [-1 for _ in range(n + 1)]
start = time.time()
print(g(n), dmemo)
end = time.time() - start
print(f'메모(딕셔너리): {int(end)}초 ({int(end * 1000000)}밀리초) 소요\n')

start = time.time()
print(h(n), lmemo)
end = time.time() - start
print(f'메모(리스트): {int(end)}초 ({int(end * 1000000)}나노초) 소요\n')

start = time.time()
print(b(n))
end = time.time() - start
print(f'바텀업: {int(end)}초 ({int(end * 1000000)}나노초) 소요\n')