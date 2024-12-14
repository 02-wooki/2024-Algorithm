# 리스트 내 키 탐색

def search(v, key, i):
    if i == len(v): return -1
    if v[i] == key: return i
    else: return search(v, key, i + 1)
        

v = [5,2,3,8,4]
print(search(v, 12, 0))