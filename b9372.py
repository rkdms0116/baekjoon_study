import sys
input = sys.stdin.readline
# T : 테스트 케이스 수
T = int(input())
# N, M : 국가의 수, 비행기의 종류
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
# a, b의 쌍 (M개)
    print(N-1)