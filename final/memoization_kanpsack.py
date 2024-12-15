
# 사전 저장소 메모이제이션
def K(n, M):
    global dictmemo, weights, profits
    if n == 0 or M == 0:                    # 더이상 물건이 없거나, 가방 공간이 초과됐을 때
        return 0

    if (n, M) in dictmemo:                      # 현재 남은 물건 수와 가방 용량에 대해 계산한 기록이 있을 때
        return dictmemo[(n, M)]
    elif M < weights[n - 1]:                # 이전에 계산한 기록이 없고, 가방에 남은 용량이 다음 물건보다 작을 때
        dictmemo[(n, M)] = K(n - 1, M)
        return dictmemo[(n, M)]
    else:                                   # 이전에 계산한 기록이 없고, 가방에 남은 용량이 다음 물건보다 클 때
        dictmemo[(n, M)] = max(K(n - 1, M), profits[n - 1] + K(n - 1, M - weights[n - 1]))
        return dictmemo[(n, M)]

# 리스트 저장소 메모이제이션
def L(n, M):
    global listmemo, weights, profits

    if listmemo[n][M] != -1: return listmemo[n][M]
    if n == 0 or M == 0: return 0

    if M < weights[n - 1]: listmemo[n][M] = L(n - 1, M)
    else: listmemo[n][M] = max(L(n - 1, M), profits[n - 1] + L(n - 1, M - weights[n - 1]))
    return listmemo[n][M]


weights = [3, 2, 2]
profits = [100, 200, 300]
capacity = 5

dictmemo = {}
listmemo = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]

print(K(len(weights), capacity))
print(dictmemo)

print(L(len(weights), capacity))
print(listmemo)