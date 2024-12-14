def bidirectional_list(V):
    g = [[] for _ in range(V)]
    E = int(input())
    for i in range(E):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    print(g)

def directed_list(V):
    g = [[] for _ in range(V)]
    E = int(input())
    for i in range(E):
        a, b = map(int, input().split())
        g[a].append(b)

    print(g)

def weighted_directed_list(V):
    g = [[] for _ in range(V)]
    E = int(input())
    for i in range(E):
        a, b, weight = map(int, input().split())
        g[a].append((b, weight))

    print(g)

def weighted_bidirectional_list(V):
    g = [[] for _ in range(V)]
    E = int(input())
    for i in range(E):
        a, b, weight = map(int, input().split())
        g[a].append((b, weight))
        g[b].append((a, weight))

    print(g)

weighted_bidirectional_list(int(input()))