n = int(input())

for _ in range(n):

    m = int(input())
    
    left = list(map(int,input().split()))
    right = list(map(int,input().split()))

    cnt = 0
    for i in range(m):
        a = left[i]
        if a+500 in left and a+1000 in right and a+1500 in right:
            cnt += 1

    print(cnt)