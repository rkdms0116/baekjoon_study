com = int(input())
pair = int(input())

graph = [[0]*(com+1) for _ in range(com+1)]

for p in range(pair):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때    
queue = [1]
result = []

while queue:
    p = queue.pop(0)

    if p not in result:
        result.append(p)
    # p인 그래프를 확인하면서 1이면서 방문하지 않았으면 추가해준다.
    for c in range(com+1):
        if graph[p][c] == 1 and c not in result:
            queue.append(c)
            graph[p][c] = 0
            graph[c][p] = 0

print(len(result)-1)