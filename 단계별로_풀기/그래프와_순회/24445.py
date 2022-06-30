# 알고리즘 수업 - 너비 우선 탐색 2
from collections import deque
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
# 정점의 수 N, 간선의 수 M, 시작 정점 R
N, M, R = map(int, input().split())
# 방문 여부 및 방문 순서 기록
visited = [0] * (N+1)
# 이중리스트로 tree 표현
tree = list([] for _ in range(N+1))
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 1
que = deque()
# bfs 함수 만들기
def bfs(v):
    global cnt
    visited[v] = cnt
    que.append(v)

    while que:
        u = que.popleft()
        node = sorted(tree[u], reverse=True)

        for n in node:
            if not visited[n]:
                que.append(n)
                visited[n] = cnt +1
                cnt += 1
# 함수 실행
bfs(R)
# 출력
for i in range(1, N+1):
    print(visited[i])
        

