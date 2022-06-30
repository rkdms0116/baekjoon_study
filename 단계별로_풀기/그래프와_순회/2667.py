# 단지번호붙이기
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
land = [list(map(int, input().rstrip())) for _ in range(N)]
# 결과 단지
danji = []
# 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a, b):
    que = deque()
    que.append([a,b])
    land[b][a] = 0
    cnt = 1
    while que:
        x, y = que.pop()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < N and -1 < ny < N and land[ny][nx] == 1:
                que.append([nx, ny])
                land[ny][nx] = 0
                cnt += 1
    return cnt


for y in range(N):
    for x in range(N):
        if land[y][x] == 1:
            danji.append(bfs(x, y))
# 출력
danji.sort()
print(len(danji))
for d in danji:
    print(d)
