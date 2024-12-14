# 합병정렬 분할정복

def merge(v, sl, el, sr, er):
    i = sl; j = sr; k = 0       # 정렬 작업에 필요한 변수들
                                #   i는 좌측 배열 인덱스, j는 우측 배열 인덱스, k는 x의 인덱스
    x = [0] * (er - sl + 1)     # er은 우측배열의 끝이므로 end, sl은 좌측 배열의 끝이므로 start

    # 정렬 수행
    #   왼쪽 배열과 오른쪽 배열 중 작은 값을 x에 먼저 넣고, x에 들어간 값의 원본 배열은 다음 인덱스로 진행
    while i <= el and j <= er:
        if v[i] < v[j]:
            x[k] = v[i]
            i += 1
        else:
            x[k] = v[j]
            j += 1
        k += 1
    
    # 오른쪽 배열이 먼저 끝난 경우 왼쪽 배열의 남은 값을 x에 삽입
    while i <= el:
        x[k] = v[i]
        i += 1
        k += 1
    
    # 왼쪽 배열이 먼저 끝난 경우 오른쪽 배열의 남은 값을 x에 삽입
    while j <= er:
        x[k] = v[j]
        j += 1
        k += 1

    # 부분문제의 해인 x를 원문제의 해당하는 인덱스에 교체
    v[sl:er + 1] = x


def sort(v, s, e):
    # 더이상 분할할 수 없는 경우 해 구하기
    # 하지만 크기 1의 배열은 이미 정렬되어있는 상태
    # 따라서 그 자체가 해이므로 별도의 작업 없음
    if (s >= e):
        return

    # 중앙값 계산
    m = s + (e - s)//2

    # 분할
    sort(v, s, m)
    sort(v, m + 1, e)

    #합병
    merge(v, s, m, m + 1, e)

array = [31, 8, 24, 3, 45, 7, 23, 11]
sort(array, 0, len(array) - 1)
print(array)