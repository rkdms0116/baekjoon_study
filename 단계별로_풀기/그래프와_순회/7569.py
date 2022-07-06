# 토마토
from collections import deque
import sys
input = sys.stdin.readline

# 상자의 가로 칸 M, 세로 칸 N, 높이 H
M, N, H = map(int,input().split())
box = []
for h in range(H):
    pan = [list(map(int, input().split()))for _ in range(N)]
    box.append(pan)

# 방향 상하좌우위아래
dx = [0,0,-1,1,0,0]
dy = [-1,1,0,0,0,0]
dz = [0,0,0,0,-1,1]

# 익은 토마토 que list에 담기
que = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                que.append((h,n,m))
# 토마토 숙성
while que:
    z, y, x = que.popleft()

    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if -1 < nz < H and -1 < ny < N and -1 < nx < M and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = box[z][y][x] + 1
            que.append((nz,ny,nx))

# 숙성시킨 뒤 토마토 박스 확인 함수
def day_cnt(box):
    max_day = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                # 익지 않은 토마토가 있을 경우 바로 return -1
                if box[h][n][m] == 0:
                    return print(-1)
                if max_day < box[h][n][m]:
                    max_day = box[h][n][m]
    else:
        return print(max_day-1)

day_cnt(box)
