# 도시 수
N = int(input())
# 여행 계획에 속한 도시들의 수
M = int(input())

city_map = []
for n in range(N):
    city = list(map(int, input().split()))
    city_map.append(city)
tour = list(map(int, input().split()))

check = [True]*N
move_connect = []

def dfs(graph, i, check):
    check[i] = False
    for j in city_map[i]:
        if city_map[j] == 1:
            city_map[j] = 0
            temp.append(j+1)
            dfs(graph, j, check)


for c in range(N):
    if check[c]:
        temp = [c+1]
        dfs()
