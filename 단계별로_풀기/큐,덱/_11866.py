# 요세푸스 문제 0
from collections import deque
# N명의 사람들, K번째 사람
N, K = map(int, input().split())
que = deque([i for i in range(1, N+1)])
# 출력 시작
print('<', end="")
while que:
    for i in range(K-1):
        que.append(que[0])
        que.popleft()
    print(que.popleft(), end = '')
    if que:
        print(', ', end="")
print('>', end="")