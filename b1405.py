import sys
input = sys.stdin.readline
# N, E 동, W 서, S 남, N 북

M, E, W, S, N = map(int, input().split())

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
location = [E/100, W/100, S/100, N/100]

robot_move = list([True]*(2*M+1) for _ in range(2*M+1))

ans = 0

def dfs(y, x, robot_move, cnt, prob):
    global ans
    if cnt == M:
        ans += prob
        return

    for d in range(4):
        sx = x + dx[d]
        sy = y + dy[d]
        if -1<sx<2*M+1 and -1<sy<2*M+1 and robot_move[sy][sx]:   
            robot_move[y][x] = False
            dfs(sy, sx, robot_move, cnt+1, prob*location[d])
            robot_move[y][x] = True
        else:
            continue

dfs(M,M,robot_move,0,1)

print(ans)