def K(n, M):
    global names, profits, weights, capacity
    nextGoods = n - 1   # 판단할 물건의 인덱스

    # n == 0인 경우: 더 이상 (선택을 결정할) 물건이 없음
    # M == 0인 경우: 더 이상 가방에 공간이 없음
    # 따라서 두 경우 모두 가방에 더 담지 않으므로 추가 이익은 0원 (재귀 탈출 조건임)
    if n == 0 or M <= 0:
        return 0

    # 다음 물건이 가방에 남은 무게보다 무거운 경우: 다음 물건은 담지 못함
    # 따라서 다음 물건은 담지 않는 것으로 결정하고, 남은 물건에 대한 결정으로 진행함 (재귀)
    # n - 1: 담지 않는 것으로 결정했으므로 남은 물건이 1 줄어듬
    # M: 담지 않는 것으로 결정했으므로 가방에 남은 공간은 그대로임
    elif M < weights[nextGoods]:
        return K(n - 1, M)

    # 가방에 공간이 있고, 선택할 물건도 남았음. 또한 다음 물건이 가방에 남은 자리보다 가벼움
    # 이 물건을 담는 것이 이득인지, 담지 않는 것이 이득인지 결정하기 위해 두 경우 모두 재귀 호출한 후, 더 큰 값을 선택
    # K(n - 1, M): 다음 물건을 담지 않는 경우를 호출함
    # profits[n - 1]: 다음 물건을 담는 경우이므로, 다음 물건의 가격을 총 이득에 더해줘야 함
    # K(n - 1, M - weights[n - 1]): 다음 물건을 담기로 결정했으므로 물건 개수는 1 줄어들어 n-1, 무게는 다음 물건만큼 줄어들어 M - weights[n-1]
    else:
        notIncludeNext = K(nextGoods, M)
        includeNext = profits[nextGoods] + K(nextGoods, M - weights[nextGoods])
        return max(notIncludeNext, includeNext)


names = ['A', 'B', 'C']
profits = [100, 300, 500]
weights = [5, 10, 25]
capacity = 30

print(K(len(names), capacity))
