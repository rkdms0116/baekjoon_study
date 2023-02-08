from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 테스트 케이스 개수 K
K = int(input())
# 정점의 개수 V, 간선의 개수 E
for _ in range(K):
    V, E = map(int, input().split())
    graph = dict()
# 그래프 연결하기
    for _ in range(E):
        u, v = map(int, input().split())
        if u-1 in graph:
            graph[u-1].append(v-1)
        else:
            graph[u-1] = [v-1]
        if v-1 in graph:
            graph[v-1].append(u-1)
        else:
            graph[v-1] = [u-1]

    check = [0]*V
    flag = 'YES'
    for c in range(V):

        if check[c] == 0:
            que = deque([c])
            check[c] = 1
            
            while que:
                v = que.popleft()
                if v in graph:
                    for n in graph[v]:

                        if check[n]==0:
                            que.append(n)
                            check[n] = -1 * check[v]
                        elif check[n] == check[v]:
                            flag = 'NO'
    
    print(flag)
