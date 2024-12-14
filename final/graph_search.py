def dfs(n):
    visited[n] = True
    print(n, '방문')
    for i in g[n]:
        if not visited[i]:
            dfs(i)

V = int(input())
E = int(input())
g = [[] for _ in range(V)]
visited = [False for _ in range(V)]
for i in range(E):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

print(g)
dfs(0)