
def ft(i, sum, left):
    global selected, list, target

    # 합이 목표에 도달한 경우 더 탐색하지 않고 바로 리턴 (탐색하지 않은 수들은 미선택 처리)
    if sum == target:
        selectedList = []
        for x in range(i):
            if selected[x]:
                selectedList.append(list[x])
        print(selectedList)
        return

    # 끝까지 탐색했는데 합이 목표에 도달하지 않은 경우는 그냥 리턴
    if i == len(list):
        return

    # sum(현재까지 합)과 list[i](더해질 수)가 목표를 초과하는 경우: list가 정렬되어 있으므로 이후에 나오는 무슨 수를 더해도 목표보다 큼. 진행할 필요 없다.
    # sum(현재까지 합)과 left(아직 고려하지 않은 모든 수의 합)가 목표 미달인 경우: 다 더해봤자 목표에 도달 못하므로 더 진행할 필요 없다.
    if sum + list[i] > target or sum + left < target:
        return

    selected[i] = False     # 이 원소를 선택하지 않는 경우
    ft(i + 1, sum, left - list[i])
    selected[i] = True     # 이 원소를 선택하는 경우
    ft(i + 1, sum + list[i], left - list[i])

target = 10
list = [2, 4, 5, 6]
list.sort()

selected = [False for _ in range(len(list))]

ft(0, 0, sum(list))