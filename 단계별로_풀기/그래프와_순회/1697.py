# 숨바꼭질
from collections import deque

# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())
visited = [0] * 100001
que = deque([N])

while que:
    now = que.popleft()
    if now == K:
        print(visited[K])
        break

    for next in [now-1, now+1, now*2]:
        if -1 < next < 100001 and visited[next]==0:
            visited[next] = visited[now] + 1
            que.append(next)

'''
# 메모리 초과
N, K = map(int, input().split())
visited = [True] * 100001
que = deque([(N, 0)])

while que:
    now, cnt = que.popleft()
    if now == K:
        print(cnt)
        break

    for next in [now-1, now+1, now*2]:
        if -1 < next < 100001 and visited[next]:
            que.append((next, cnt + 1))
'''