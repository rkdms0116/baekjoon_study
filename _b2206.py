dx = [1,0,-1,0]
dy = [0,1,0,-1]

def miro_find(arr,x,y,chance):
    global cnt, visited

    if x == M-1 and y == N-1:
        return cnt
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx]==0:
            if arr[ny][nx] == '1' and chance > 0:
                visited[nx][ny] = 1
                cnt += 1
                miro_find(arr,nx,ny,0)
                cnt -= 1
                visited[nx][ny] = 0
            elif arr[ny][nx] == '0':
                visited[ny][nx] = 1
                cnt += 1
                miro_find(arr,nx,ny,chance)
                cnt -= 1
                visited[nx][ny] = 0

# 세로, 가로
N, M = map(int,input().split())

miro = [list(input()) for _ in range(N)]
visited = list([0]*M for _ in range(N))
cnt = 1
print(miro_find(miro,0,0,1))