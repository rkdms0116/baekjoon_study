import sys
sys.setrecursionlimit(10000)

dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,-1,1,-1,1]

def som(y,x):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < w and 0 <= ny < h:
            if nara[ny][nx] == 1:
                nara[ny][nx] = 0
                som(ny, nx)


# 입력값 받기
while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    nara = [list(map(int, input().split())) for _ in range(h)]
    visited = list([0]*w for _ in range(h))
    cnt = 0

    for i in range(h):
        for j in range(w):
            if nara[i][j] == 1:
                som(i, j)
                cnt += 1
    
    print(cnt)