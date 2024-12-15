import math

def C(money):
    global coin
    if money == 0:
        return 0
    elif money < 0:
        return math.inf
    else:
        return 1 + min([C(money - i) for i in coin])

def memoC(money):
    global coin, memo
    if money in memo:
        return memo[money]

    if money == 0:
        return 0
    elif money < 0:
        return math.inf
    else:
        memo[money] = 1 + min([memoC(money - i) for i in coin])
        return memo[money]

def memoListC(money):
    global coin, listMemo
    if money < 0:                   # 남은 금액이 0 이하일 경우
        return math.inf
    elif listMemo[money] != -1:     # 계산한 기록이 있는 경우 (0 이상일 떄): 바로 반환
        return listMemo[money]
    elif money == 0:                # 남은 금액이 0일 떄: 0 기록 후 반환
        listMemo[money] = 0
    else:                           # 남은 금액이 양수일 때: 재귀호출로 모든 경우의 수 중 가장 작은 결과 기록 후 반환
        listMemo[money] = 1 + min([memoListC(money - i) for i in coin])
    return listMemo[money]

def F(money):
    global coin, listMemo, P
    if money >= 0 and listMemo[money] != -1:
        return listMemo[money]
    elif money < 0:
        return math.inf
    elif money == 0:
        return 0

    count = math.inf
    coinUsed = -1                   # 최적해에 사용된 동전 액면가를 저장하는 변수
    for i in coin:
        newCount = 1 + F(money - i)
        if newCount < count:            # 지금까지 계산된 동전 개수중 가장 작다면
            count = newCount            # 동전 개수 갱신
            coinUsed = i                # 최적해에 사용된 동전 저장
    listMemo[money] = count         # 최적해 동전 개수 메모
    P[money] = coinUsed             # 최적해에 사용된 동전 액면가 기록
    return count

def printF(money):
    global listMemo, P
    if listMemo[money] == -1 or listMemo[money] == math.inf:
        print('교환 불가')
        return
    usedMoney = []
    while money > 0:
        usedMoney.append(P[money])
        money -= P[money]
    print(usedMoney)

def bottomup(money):
    global coin
    dp = [0 for _ in range(money + 1)]

    for i in range(1, money + 1):
        dp[i] = 1 + min([dp[i - j] if i >= j else math.inf for j in coin])

    print(dp)
    return dp[money]

memo = {}
listMemo = []
P = []

coin = [5, 10]
moneys = [15, 3, 30, 20]

for i in moneys:
    memo = {}
    listMemo = [-1] * (i + 1)
    P = [-1] * (i + 1)
    print(f'\t\tC({i}):', C(i))
    print(f'\tmemoC({i}):', memoC(i))
    print(f'memoListC({i}):', memoListC(i))
    listMemo = [-1] * (i + 1)
    print(f'\t\tF({i}):', F(i))
    printF(i)
    print(bottomup(i))

memo = {}
coin = [2, 3, 4]
print(C(6))

# coin = [1, 5, 10, 20, 25]
# print(C(65))