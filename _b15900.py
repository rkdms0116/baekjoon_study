def dfs(i, cnt):

    while stack:
        v, c = stack.pop()
        if v not in visited:
            visited[v] = 1

            for i in range(tree[v]):
                if i not in visited:
                    stack.append([v, c+1])

N = int(input())

tree = [[0]*(N+1) for _ in range(N+1)]
stack = [[1,0]]
visited = [0]*(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a][b] = 1
    tree[b][a] = 1

