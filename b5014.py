from collections import deque

# F층까지 있는 건물
# 강호가 현재 있는 층 : S층 
# 목표 층 : G
# U : up, D : down
F, S, G, U, D = map(int, input().split())

building = [0] * (F+1)
def bfs():
    que = deque([S])
    building[S] = 1
    dir = [U, (-1)*D]
    while que:
        now = que.popleft()
        
        if now == G:
            return building[G]-1

        for d in range(2):
            next = now + dir[d]

            if 0 < next < F+1 and not (building[next]):
                building[next] = building[now] + 1
                que.append(next)

    return 'use the stairs'

print(bfs())