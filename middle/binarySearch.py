# 이진탐색 분할정복

def search(v, s, e, key):
    
    # 배열 크기가 0이 되면 찾는 값이 없으므로 -1 반환
    if (s > e):
        return -1
    
    # 중앙값 계산
    m = s + (e - s)//2
    
    # 중앙값과 키 비교하여 분할 혹은 해 계산
    #   key < v[m]: 키가 중앙값보다 작을 때 - 중앙보다 왼쪽으로 분할
    #   key > v[m]: 키가 중앙값보다 클 때 - 중앙보다 오른쪽으로 분할
    #   key == m: 키와 중앙값이 일치 할 때 - 찾았으므로 중앙의 인덱스를 반환
    if (key < v[m]):
        return search(v, s, m - 1, key)
    elif (key > v[m]):
        return search(v, m + 1, e, key)
    else:
        return m



array = [3, 7, 8, 11, 23, 24, 31, 45]   
print(search(array, 0, len(array) - 1, 25))