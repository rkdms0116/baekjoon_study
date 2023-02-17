def fibo(n, ans):
    if n==0:
        ans[0] += 1
        return 0
    elif n==1:
        ans[1] += 1
        return 1
    else:
        return fibo(n-1,ans) + fibo(n-2,ans)
    

T = int(input())
for _ in range(T):
    N = int(input())
    ans = [0, 0]
    fibo(N,ans)
    print(' '.join(map(str, ans)))
