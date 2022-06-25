from collections import deque
import sys
input = sys.stdin.readline

dy = [-1,-2,-2,-1,1,2,2,1]
dx = [-2,-1,1,2,2,1,-1,-2]

def move():
    global result

    while que:
        y, x = que.popleft()

        if x == ex and y == ey:
            return

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]

            if -1 < nx < I and -1 < ny < I and chess[ny][nx] == 0:
                result = chess[y][x] + 1
                chess[ny][nx] = result
                que.append((ny, nx))

T = int(input())

for tc in range(1, T+1):
    # chess(I*I) 한 줄 크기
    I = int(input())
    chess = [[0]*I for _ in range(I)]

    que = deque()
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    chess[sy][sx] = 1
    que.append((sy, sx))

    result = 0
    move()

    if result > 2:
        result -= 2

    print(result)