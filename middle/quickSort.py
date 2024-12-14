# 퀵 정렬 분할정복

def sort(v, low, high):

    print(v[low: high + 1])

    # 더 이상 분할할 수 없으면 정렬을 수행하지만, 크기 1 배열은 이미 정렬된 상태: no further action
    if (low >= high):
        return
    
    # i는 LTEQ 배열의 end
    i = low - 1
    pivot = v[high]

    # pivot보다 작은 값과 큰값 분리
    #   pivot보다 작거나 같은 값을 발견하면 v[i]와 해당 값의 위치를 바꿈으로써 LTEQ 배열이 확장됨
    for j in range(low, high):
        if v[j] > pivot:
            continue
        
        i += 1; swap(v, i, j)

    # 분리가 끝나면 v[low:i + 1]은 LTEQ (작거나 같은 값), v[i + 1: high]는 GT, v[high]는 pivot값
    # 따라서 i+1에 있는 값이랑 pivot에 있는 값이랑 위치를 바꿔주면 pivot의 위치를 기준으로 완전히 분리된다.
    i += 1
    swap(v, high, i)

    sort(v, low, i - 1)
    sort(v, i + 1, high)
    
    
def swap(v, i, j):
    tmp = v[i]; v[i] = v[j]; v[j] = tmp




array = [2, 8, 7, 1, 3, 5, 6, 4]
sort(array, 0, len(array) - 1)
print(array)