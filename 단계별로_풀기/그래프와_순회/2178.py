# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]

# 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# bfs 사용 > 최단거리
que = deque([(0, 0)])
while True:
    y, x = que.popleft()
    if y == N-1 and x == M-1:
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if -1 < nx < M and -1 < ny < N and miro[ny][nx] == 1:
            miro[ny][nx] = miro[y][x] + 1
            que.append((ny,nx))

print(miro[N-1][M-1])