list = [3, 7, 2, 5, 3, 4, 8]

# 최대값 찾기
maxValue = -1
for i in list:
    maxValue = i if i > maxValue else maxValue

count = [0 for _ in range(maxValue + 1)]
for i in list:
    count[i] += 1

print(count)

result = []
for i in range(len(count)):
    while count[i] > 0:
        result.append(i)
        count[i] -= 1

print(result)