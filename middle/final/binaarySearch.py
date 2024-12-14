# 이진탐색

def search(v, s, e, key):
    if s > e:
        return -1
    
    m = s + (e-s)//2
    if v[m] > key:
        return search(v, s, m - 1, key)
    elif v[m] < key:
        return search(v, m + 1, e, key)
    else:
        return m
    
def searchRepeat(v, key):
    s, e = 0, len(v) - 1
    while s <= e:
        m = s + (e - s) // 2
        if v[m] > key:
            e = m
        elif v[m] < key:
            s = m + 1
        else:
            return m
    return -1
    
    
v = [9, 3, 4, 2, 8, 1, 7, 4]
v.sort()
print(v)
for i in range(10):
    print(i, ": index ", searchRepeat(v, i))