import sys
input = sys.stdin.readline

# 아래와 오른쪽 이동 방향
dx = [0, 1]
dy = [1, 0]

N = int(input())
game_map = []
# game_map 받기
for _ in range(N):
    game_map.append(list(map(int, input().split())))

# 시작점 만들기
visit = list([False]*N for _ in range(N))
stack = [[0,0]]
result = 'Hing'

while stack:
    st = stack.pop()
    sy = st[0]
    sx = st[1]
    visit[sy][sx] = True
    
    # 완료 조건
    if sx == N-1 and sy == N-1:
        result = 'HaruHaru'
        break
    
    value = game_map[sy][sx]
    
    for i in range(2):
        nx = sx + dx[i]*value
        ny = sy + dy[i]*value
        # 범위를 넘지 않고 방문하지 않았으면 stack에 넣어줍니다.
        if -1 < nx < N and -1 < ny < N and visit[ny][nx] == False:
            stack.append([ny, nx])

print(result)