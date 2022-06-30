# 알고리즘 수업 - 깊이 우선 탐색 1
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
    # 양방향 tree
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 1
# dfs 함수 만들기
def dfs(v):
    global cnt
    visited[v] = cnt
    # 정렬이 안되어있으므로 정렬
    tree[v].sort()

    for t in tree[v]:
        if visited[t] == 0:
            cnt += 1
            dfs(t)
# 함수 실행
dfs(R)
# 출력
for i in range(1, N+1):
    print(visited[i])