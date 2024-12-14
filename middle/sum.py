# 리스트 내 정수 총합

def sum(v, i):
    if i == len(v): return 0
    return v[i] + sum(v, i + 1)

print(sum([1,2,3,4,5], 0))