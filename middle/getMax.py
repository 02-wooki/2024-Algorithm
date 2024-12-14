# 분할정복 추가 자료 - 배열 최대값 찾기

def getMax(v, s, e):
    if s == e: return v[s]

    m = s + (e - s)//2
    l = getMax(v, s, m)
    r = getMax(v, m + 1, e)

    if l > r: return l
    else: return r

def getMin(v, s, e):
    if s == e: return v[s]

    m = s + (e - s) // 2
    l = getMin(v, s, m)
    r = getMin(v, m + 1, e)

    if l < r: return l
    else: return r

print(getMax([3,5,6,9,2,4,1,11], 0, 7))