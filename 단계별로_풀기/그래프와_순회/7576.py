# 토마토
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = list([int(i) for i in input().split()] for _ in range(N))

# 방향
dy = [0,0,-1,1]
dx = [-1,1,0,0]
que = deque()
for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            que.append((y,x))

while que:
    y, x = que.popleft()

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]

        if -1 < ny < N and -1 < nx < M and box[ny][nx] == 0:
            que.append((ny,nx))
            box[ny][nx] = box[y][x] +1

# 토마토 숙성 날짜 확인
def tomato_day(box):
    max_day = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return print(-1)
            if box[i][j] > max_day:
                max_day = box[i][j]
    else:
        return print(max_day-1)

tomato_day(box)