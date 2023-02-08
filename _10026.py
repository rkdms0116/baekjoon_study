from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 크기
N = int(input())
# 색상 판
color_boards = []
for _ in range(N):
    color_boards.append(list(input()))
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n_visited = [[True]*N for _ in range(N)]
# 일반인이 보는 색상 판
def normal(boards, y, x, visited):
    color = color_boards[y][x]
    que = deque([(y,x)])
    while que:
        y, x = que.popleft()
        visited[y][x] = False
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if -1 < ny < N and -1 < nx < N and boards[ny][nx] == color and visited[ny][nx]:
                que.append((ny,nx))
# bfs로 체크
n_cnt = 0
for j in range(N):
    for i in range(N):
        if n_visited[j][i]:
            normal(color_boards, j, i, n_visited)
            n_cnt += 1

# # 적록색약이 보는 색상 판
# def dys(boards, y, x, visited):
#     # 적록색약
#     if color_boards[y][x] == 'R' or color_boards[y][x] == 'G':
#         color = ['R', 'G']
#     else:
#         color = ['B']
#     que = deque([(y,x)])
#     while que:
#         y, x = que.popleft()
#         visited[y][x] = False
#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]
#             if -1 < ny < N and -1 < nx < N and boards[ny][nx] in color and visited[ny][nx]:
#                 que.append((ny,nx))

d_visited = [[True]*N for _ in range(N)]
d_cnt = 0
for j in range(N):
    for i in range(N):
        if color_boards[j][i]=='G':
            color_boards[j][i]='R'

for j in range(N):
    for i in range(N):
        if d_visited[j][i]:
            normal(color_boards, j, i, d_visited)
            d_cnt += 1
print(n_cnt, d_cnt)

# 일반 색상 판에서 R과 G를 동일하게 판단