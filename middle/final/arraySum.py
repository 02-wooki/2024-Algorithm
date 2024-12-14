# 배열 합

def sum(v, s, e):
    if s == e:
        return v[s]
    
    m = s + (e - s)//2
    l = sum(v, s, m)
    r = sum(v, m + 1, e)

    return l + r

v = [9, 3, 4, 2, 8, 1, 7, 4]
print(sum(v, 0, len(v)-1))