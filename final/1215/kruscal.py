# find 연산 (루트 찾기)
def find(n):
    global parent
    if parent[n] == n:
        return n
    else:
        parent[n] = find(parent[n])     # 경로압축
        return parent[n]

# union 연산 (합집합)
def union(x, y):
    global parent, rank
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] == rank[y]:
        parent[x] = y
        rank[y] += 1
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y

def K():
    global parent, rank, edges, N
    edges.sort(key = lambda x: x[2])    # 가중치 기준 오름차순 정렬

    cost = 0
    mst = []
    for S, E, W in edges:
        if len(mst) >= N - 1: break
        if find(S) != find(E):
            union(S, E)
            mst.append((S, E))
            cost += W

    return (cost, mst) if len(mst) == N - 1 else ([], -1)


N = 7
parent = [i for i in range(N)]
rank = [0 for _ in range(N)]
edges = [(0, 1, 28), (0, 5, 10), (1, 2, 16), (1, 6, 14), (2, 3, 12), (3, 4, 22), (3, 6, 18), (4, 5, 25), (4, 6, 24)]

print(K())