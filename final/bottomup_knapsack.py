
def K(n, m, W, P):
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):                      # i는 현재 담을지 말지 결정한 물건의 개수 & i-1은 현재 결정중인 물건의 인덱스를 의미
        for j in range(m + 1):                  # j는 현재 사용한 가방의 용량을 의미
            if i == 0 or j == 0: dp[i][j] = 0       # 가방에 담을 물건이 없거나 가방 용량이 없는 경우
            elif j < W[i - 1]: dp[i][j] = dp[i - 1][j]  # 가방에 담지 않는 경우 (가방 용량 부족)
            else:                                   # 가방 용량 충분한 경우: 담을지, 담지 않을지 결정
                dp[i][j] = max(dp[i - 1][j], P[i - 1] + dp[i - 1][j - W[i - 1]])
    return dp[n][m]

capacity = 5
weights = [3, 2, 2]
profits = [100, 200, 300]

print(K(len(weights), capacity, weights, profits))