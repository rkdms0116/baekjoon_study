N, M = map(int, input().split())
a = [0] + list(map(int,input().split()))

i = 1
case = 1
while i < N and M > 0:
    if i+2 < N:
        case1 = case + a[i+1]
        case2 = case//2 + a[i+2]
        if case1 < case2:
            i += 1
        case = max(case1, case2)
    else:
        case += a[i+1]
    i += 1
    M -= 1

print(case)