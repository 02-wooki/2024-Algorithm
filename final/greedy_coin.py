def coinchange(money, coin):
    coin.sort(reverse=True) # 액면가 내림차순으로 정렬
    exchange = []
    for i in range(len(coin)):
        if coin[i] > money:
            continue
        exchange.append((coin[i], money // coin[i]))        # 해당 액면가로 몇 개 거스르는지
        money %= coin[i]                                    # 해당 액면가로 거스른 후 얼마가 남는지

    # 주어진 액면들로 거스를 수 있으면 거스른 결과를 반환하고 그렇지 않으면 빈 배열 반환
    return [] if money != 0 else exchange

print(coinchange(54320, [5, 10, 50, 100, 500, 1000, 5000]))