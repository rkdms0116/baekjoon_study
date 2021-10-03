com = int(input())
pair = int(input())

node = []
graph = [[0]*(com+1) for _ in range(com+1)]

for i in range(pair):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

stack = [1]
visited = []

while stack:
    a = stack.pop(0)

    if a not in visited:
        visited.append(a)

    for j in range(com+1):
        if graph[a][j] == 1 and j not in visited:
            stack.append(j)
            graph[a][j] = 0
            graph[j][a] = 0

print(len(visited)-1)

