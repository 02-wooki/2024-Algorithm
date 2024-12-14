def printGraph(graph):
    for i in graph:
        print(i)

def bidirectional_graph(V):
    g = [[0 for _ in range(V)] for _ in range(V)]       # 2차원 배열 생성 및 초기화
    E = int(input())                                    # 간선 개수 입력
    for _ in range(E):                                  # 간선 입력받아서 인접행렬에 추가하는 반복문
        x, y = map(int, input().split())
        g[x][y] = 1
        g[y][x] = 1

    print(g)

def directed_graph(V):
    g = [[0 for _ in range(V)] for _ in range(V)]
    E = int(input())
    for _ in range(E):
        x, y = map(int, input().split())
        g[x][y] = 1

    print(g)

def weighted_bidirectional_graph(V):
    g = [[0 for _ in range(V)] for _ in range(V)]
    E = int(input())
    for _ in range(E):
        x, y, weight = map(int, input().split())
        g[x][y] = weight
        g[y][x] = weight

    print(g)

def weighted_directed_graph(V):
    g = [[0 for _ in range(V)] for _ in range(V)]
    E = int(input())
    for _ in range(E):
        x, y, weight = map(int, input().split())
        g[x][y] = weight

    print(g)

weighted_bidirectional_graph(int(input()))