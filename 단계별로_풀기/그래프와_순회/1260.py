# DFS와 BFS
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 번호 V
N, M, V = map(int, input().split())
# 양방향 tree 만들기
tree = list([] for _ in range(N+1))
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# dfs
dfs_visit = []
visited_dfs = [False] * (N+1)
def dfs(v):
    if v not in dfs_visit:
        visited_dfs[v] = True
        dfs_visit.append(v)
    tree[v].sort()
    for t in tree[v]:
        if not visited_dfs[t]:
            dfs(t)

dfs(V)
print(" ".join(map(str,dfs_visit)))

# bfs
bfs_visit = []
visited_bfs = [False] * (N+1)
que = deque()

def bfs(v):
    visited_bfs[v] = True
    que.append(v)

    while que:
        q = que.popleft()
        if q not in bfs_visit:
            bfs_visit.append(q)
        
        tree[q].sort()
        for t in tree[q]:
            if not visited_bfs[t]:
                visited_bfs[t] = True
                que.append(t)

bfs(V)
print(" ".join(map(str,bfs_visit)))
