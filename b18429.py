# 순열 구현
def perm(li):
    if len(li) == 0:
        return []
    elif len(li) == 1:
        return [li]
    else:
        l = []
        for i in range(len(li)):
            x = li[i]
            x_remain = li[:i] + li[i+1:]
            for t in perm(x_remain):
                l.append([x]+t)
        return l

# N일, 하루마다 K만큼 중량 감소
N, K = map(int,input().split())
# N일간의 운동 list
A = list(map(int,input().split()))

cnt = 0
# permutaion으로 만들어진 함수에서 하나씩 빼보면서
for a in perm(A):
    total = 0
    for n in range(N):
        if total + a[n] - K < 0:
            break
        else:
            total += a[n]-K
    else:
        cnt += 1

print(cnt)