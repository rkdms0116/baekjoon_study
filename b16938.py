# 캠프 준비

# N : 문제 개수, L <= 문제의 난이도 합 <= R, (가장어려운문제)-(가장쉬운문제)>=X
N, L, R, X = map(int, input().split())
# N개의 문제 list
problems = list(map(int, input().split()))
# 시험 문제
test = []
for p in range(1,1<<N):
    hubo = []
    for i in range(N):
        if p & (1 << i):
            hubo += [problems[i]]
    if L <= sum(hubo) <= R and max(hubo)-min(hubo) >= X:
        test.append(list(hubo))
    
print(len(test))