def find(x, parent):
    while parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, parent, rank):
    x = find(x, parent)
    y = find(y, parent)

    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1


def K(n, E):
    E.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]

    i = 0
    mst, mstSize = [], 0
    cost = 0
    while mstSize < n - 1 and i < len(E):
        s, e, w = E[i]
        if find(s, parent) != find(e, parent):
            mst.append((s, e))
            mstSize += 1
            union(s, e, parent, rank)
            cost += w
        i += 1

    if mstSize < n - 1:
        return [], -1
    else:
        return mst, cost

n = 7
E = [(0, 1, 28), (0, 5, 10), (1, 2, 16), ]