
def union(x, y, parent, rank):        # x가 속한 집합과 y가 속한 집합의 합집합 생성
    x = find(x, parent)
    y = find(y, parent)
    if x == y:          # x와 y가 같은 집합에 속한 경우 합집합 수행 불필요
        return

    # 랭크가 작은 쪽이 랭크가 큰 쪽 밑으로 딸려가게
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        rank[y] += 1 if rank[x] == rank[y] else 0


def find(x, parent):            # x의 루트를 찾아서 반환
    while parent[x] != x:       # 경로 압축 (모든 상위 노드들의 부모를 루트로 바꿈)
        x = parent[x]
        parent[x] = find(parent[x], parent)
    return parent[x]

def kruskal(N, E):
    E.sort(key = lambda e: e[2])        # 가중치 기준 정렬
    parent = [i for i in range(N)]
    rank = [0 for _ in range(N)]

    i = 0
    numEdge = len(E)            # 간선의 개수
    mst, mstSize = [], 0        # 최소비용신장트리와 그 길이
    cost = 0                    # 완성된 최소비용신장트리의 총 비용

    # 간선을 모두 사용하기 전까지, 그리고 경로의 길이가 (노드 - 1)개를 넘기 전까지
    while i < numEdge and mstSize < N - 1:
        x, y, weight = E[i]     # 연결할 간선의 양쪽 노드와 가중치
        if find(x, parent) != find(y, parent):  # Cycle 판단 (두 원소의 루트가 같으면 Cycle 발생)
            mst.append(E[i])        # 트리에 간선 추가
            mstSize += 1            # 트리의 경로 길이 1 증가
            cost += weight          # 트리 비용 증가
            union(x, y, parent, rank)             # 합집합
        i += 1

    # 최소비용신장트리의 경로 길이가 (노드 - 1)개를 충족하지 못하면 빈 트리와 -1의 가중치를 반환,
    # 충족하면 만들어진 최소비용신장트리와 가중치 반환
    if mstSize < N - 1:
        return [], -1
    else:
        return mst, cost

N = 7
edge = [(0, 1, 28), (0, 5, 10), (1, 2, 16), (1, 6, 14), (2, 3, 12), (3, 4, 22), (3, 6, 18), (4, 5, 25), (4, 6, 24)]

print(kruskal(N, edge))