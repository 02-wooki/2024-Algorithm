# 양방향 그래프 인접리스트
from collections import deque


def nearList(N, E):
    A = [[] for _ in range(N)]
    for s, e in E:
        A[s].append(e)
        A[e].append(s)
    return A

# 양방향 그래프 인접행렬
def nearTable(N, E):
    A = [[0 for _ in range(N)] for _ in range(N)]
    for s, e in E:
        A[s][e] = 1
        A[e][s] = 1
    return A

# 깊이우선탐색
def dfs(v):
    global A, visited
    visited[v] = True
    print(v, '->', end=' ')

    for i in A[v]:
        if not visited[i]:
            dfs(i)

def dfs_loop(v):
    global A, visited
    stack = [v]

    while stack:
        v = stack.pop(-1)
        visited[v] = True
        print(v, '->', end=' ')

        for i in A[v]:
            if not visited[i]:
                stack.append(i)

def bfs(v):
    global visited, A
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        visited[v] = True
        print(v, '->', end=' ')

        for i in A[v]:
            if not visited[i]:
                queue.append(i)

N = 5
E = [(0, 1), (0, 2), (3, 1), (2, 4)]

visited = [False for _ in range(N)]
A = nearList(N, E)

print(A)
dfs(3)

visited = [False for _ in range(N)]
print('')
dfs_loop(3)

visited = [False for _ in range(N)]
print('')
bfs(0)