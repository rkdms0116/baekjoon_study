# 크기
N = int(input())
# 색상 판
color_boards = []
for _ in range(N):
    color_boards.append(list(input()))

# 일반인이 보는 색상 판
def normal(boards):
    cnt = 0
    # 상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
# 0 ~ N-1 까지 돌아보면서(상하좌우)
    for i in range(N):
        for j in range(N):
# bfs로 체크

# 적록색약이 보는 색상 판
# 일반 색상 판에서 R과 G를 동일하게 판단