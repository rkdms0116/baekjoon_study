from collections import deque

# 상자의 가로 M, 세로 N
M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

tomato = deque()

for j in range(N):
    for i in range(M):
        if box[j][i] == 1:
            tomato.append((j,i))

dy = [-1,1,0,0]
dx = [0,0,-1,1]
day = 0

while tomato:
    y, x = tomato.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
            day = box[y][x] + 1
            box[ny][nx] = day
            tomato.append((ny,nx))

# 익지 않은 토마토가 있을 경우 불가능 -1
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            day = -1

if day > 1:
    day -= 1

print(day)
