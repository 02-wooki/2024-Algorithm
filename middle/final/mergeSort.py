# 합병정렬

def merge(v, s1, e1, s2, e2):
    i, j, k, x = s1, s2, 0, [0] * (e2 - s1 + 1)

    while i <= e1 and j <= e2:
        if v[i] < v[j]:
            x[k] = v[i]
            k += 1; i += 1
        else:
            x[k] = v[j]
            k += 1; j += 1

    while i <= e1:
        x[k] = v[i]
        k += 1; i += 1
    while j <= e2:
        x[k] = v[j]
        k += 1; j += 1

    v[s1:e2 + 1] = x

def mergeSort(v, s, e):
    if s >= e:
        return
    
    m = s + (e - s)//2
    mergeSort(v, s, m)
    mergeSort(v, m + 1, e)

    merge(v, s, m, m+1, e)

v = [9, 3, 4, 2, 8, 1, 7, 4]
mergeSort(v, 0, len(v) - 1)
print(v)