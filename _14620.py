# 화단의 한 변의 길이 N
N = int(input())
# 1 ~ N-2까지 상하좌우 합친 가격으로 화단을 변형시킨다.
farms = list()
for _ in range(N):
    farms.append(list(map(int, input().split())))
# 한 칸 이상 건너띄면서 최솟값 찾기
cost_land = []
dy = [-1,1,0,0,0]
dx = [0,0,-1,1,0]
for i in range(1, N-1):
    for j in range(1, N-1):
        cost = 0
        for d in range(5):
            cost += farms[j+dy[d]][i+dx[d]]
        cost_land.append((cost, (j,i)))
cost_land.sort(key= lambda x:x[0])

land = set()
pay = 0
for c in cost_land:
    cost, (land_y, land_x) = c
    temp_land = set()
    for d in range(5):
        temp_land.add(tuple([land_y+dy[d],land_x+dx[d]]))
    if not(len(land|temp_land)%5):
        pay += cost
        land = land|temp_land
    if len(land) == 15:
        print(pay)
        break
