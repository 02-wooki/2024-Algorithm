# 리스트 내 최대값

def great(v, i):
    if i == len(v) - 1: return v[i]
    return max(v[i], great(v, i + 1))

print(great([5,2,8,3,4], 0))