import sys
sys.setrecursionlimit(10000)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def jeerung(y,x):
    for t in range(4):
        ny = y + dy[t]
        nx = x + dx[t]

        if 0 <= ny < N and 0 <= nx < M and vat[ny][nx] == 1:
            vat[ny][nx]=0
            jeerung(ny,nx)

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())

    vat = [[0]*M for _ in range(N)]

    for k in range(K):
        X, Y = map(int, input().split())
        vat[Y][X] = 1

    cnt = 0

    for y in range(N):
        for x in range(M):
            if vat[y][x] == 1:
                jeerung(y,x)
                cnt += 1

    print(cnt)