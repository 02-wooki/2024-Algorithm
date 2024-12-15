# 0/1 배낭 문제 (0-인덱싱)

# 단순 재귀 구현
def R(n, M):
    global weight, profit

    if n == 0 or M == 0:
        return 0
    elif M < weight[n - 1]:
        return R(n - 1, M)
    else:
        return max(R(n - 1, M), profit[n - 1] + R(n - 1, M - weight[n - 1]))

# 메모이제이션(딕셔너리)
def DR(n, M):
    global weight, profit, dmemo

    if (n, M) in dmemo:
        return dmemo[(n, M)]

    if n == 0 or M == 0:
        return 0
    elif M < weight[n - 1]:
        dmemo[(n, M)] = DR(n - 1, M)
    else:
        dmemo[(n, M)] = max(DR(n - 1, M), profit[n - 1] + DR(n - 1, M - weight[n - 1]))
    return dmemo[(n, M)]

# 메모이제이션(리스트)
def LR(n, M):
    global weight, profit, lmemo

    if lmemo[n][M] != -1:
        return lmemo[n][M]

    if n == 0 or M == 0:
        return 0
    elif M < weight[n - 1]:
        lmemo[n][M] = LR(n - 1, M)
    else:
        lmemo[n][M] = max(LR(n - 1, M), profit[n - 1] + LR(n - 1, M - weight[n - 1]))
    return lmemo[n][M]

# 바텀업
def BU(n, M):
    global weight, profit
    dp = [[-1 for _ in range(M + 1)] for _ in range(len(weight) + 1)]

    for i in range(n + 1):
        for j in range(M + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j < weight[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], profit[i - 1] + dp[i - 1][j - weight[i - 1]])

    return dp[n][M], dp

# 조건: 배낭에 담을 수 있는 무게는 5kg
# [0]: 무게 3kg, 가격 100
# [1]: 무게 2kg, 가격 200
# [2]: 무게 2kg, 가격 300
weight = [3, 2, 2]
profit = [100, 200, 300]
capacity = 5

print(R(len(weight), capacity))

dmemo = {}
lmemo = [[-1 for _ in range(capacity + 1)] for _ in range(len(weight) + 1)]
print(DR(len(weight), capacity), dmemo)
print(LR(len(weight), capacity), lmemo)

print(BU(len(weight), capacity))