# 배열 합 분할정복

def sum(v, s, e):
    
    # 더이상 분해되지 않는 경우
    if (s == e):
        print('call stack endpoint [', s, ']:', v[s])
        return v[s]
    
    print('sum(', v, ', ', s, ', ', e, ')')

    # 중앙값 계산
    m = s + (e - s)//2

    # 부문제 각각 해결
    l = sum(v, s, m)
    r = sum(v, m + 1, e)

    # 부문제의 해 결합 (원문제의 해 계산)
    return l + r


# array = list(map(int, input().split()))
array = [3, 5, 6, 9, 2, 4, 1, 8]
print(sum(array, 0, len(array) - 1))