N, M = map(int, input().split())
vat = list(map(int, input().split()))
cnt = 0
i = 0
snow_size = 1

while i < N:
    if cnt == M:
        break
    
    snow_size1 = snow_size + vat[i+1]
    snow_size2 = snow_size//2 + vat[i+2]

    if snow_size1 >= snow_size2:
        i += 1
        snow_size = snow_size1
    else:
        i += 2
        snow_size = snow_size2

    cnt += 1

print(snow_size)


'''N, M = map(int, input().split())
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

print(case)'''