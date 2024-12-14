# 리스트 내 각 정수 1 증가

def add(v, i):
    if i < len(array):
        v[i] += 1
        return add(v, i + 1)

array = [5, 2, 7, 3, 4]
add(array, 0)
print(array)