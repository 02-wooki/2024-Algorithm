v = int(input())
charge = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
chargeSum = [0] * len(charge)

for i in range(len(charge)):
    while (v >= charge[i]):
        chargeSum[i] += 1
        v -= charge[i]
    print(charge[i], "원권 ",chargeSum[i], "개")