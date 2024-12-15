def knapsack(names, weights, values, M):
    goods = [(names[i], weights[i], values[i]) for i in range(len(names))] # (이름, 무게, 가격) 리스트
    goods.sort(key = lambda x: x[2]/x[1], reverse=True)                    # 무게당 가격의 역순으로 정렬

    sumValue = 0
    result = []
    for n, w, v in goods:
        if M >= w:
            sumValue += v
            result.append((n, 1))
            M -= w
        else:
            sumValue += v * M/w          # M/w는 총 무게 대비 담을 수 있는 무게의 비율, 따라서 v * M/w는 담은 무게만큼의 가격
            result.append((n, M/w))
            M = 0

    return result, sumValue

names = ['A', 'B', 'C']
weights = [10, 20, 5]
values = [150, 100, 150]
capacity = 20

print(knapsack(names, weights, values, capacity))