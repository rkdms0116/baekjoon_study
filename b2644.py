N = int(input())

s, e = map(int, input().split())

M = int(input())

chon = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    x, y = map(int, input().split())
    chon[x][y] = 1
    chon[y][x] = 1

stack = [s]
visited = []
cnt = -1

while stack:
    a = stack.pop(0)

    if a not in visited:
        visited.append(a)

    for j in range(M+1):
        if chon[a][j] == 1:
            stack.append(j)
            chon[a][j] = 0
            chon[j][a] = 0
    cnt += 1

print(cnt)