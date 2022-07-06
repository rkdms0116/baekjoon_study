# 알고리즘 수업 - 피보나치 수 1
import sys
sys.setrecursionlimit(10**8)


n = int(input())

def recur(n):
    if n == 1 or n == 2:
        return 1
    return recur(n-1) + recur(n-2)

# def dynamic(n):
#     fibo = [0] * (n+1)
#     fibo[1] = fibo[2] = 1
#     cnt = 0
#     for i in range(3, n+1):
#         cnt += 1
#         fibo[i] = fibo[i-1] + fibo[i-2]
#     return cnt

print(recur(n), n-2)

"""
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
def fibonacci(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    cnt2=0
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n=int(input())
print(fib(n),fibonacci(n))
"""