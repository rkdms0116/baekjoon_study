import math

# 소수 찾는 함수
def prime(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if not(n%i):
            return False
    else:
        return True

# 팰린드롬 확인 함수
def palin(n):
    str_n = str(n)
    if str_n == str_n[::-1]:
        return True
    else:
        return False


N = int(input())
while True:
    if palin(N) and prime(N):
        print(N)
        break
    else:
        N += 1
