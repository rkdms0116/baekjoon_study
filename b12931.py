# B 배열의 크기 N
N = int(input())
# B list
B = list(map(int, input().split()))

A = [0]*N
cnt = 0
while True:
    for i in range(N):
        # 홀수가 있다면
        if B[i]%2:
            B[i] -= 1
            cnt += 1
    # 짝수로 만든 뒤 A==B라면 while문 종료
    if A==B:
        break
    # 아닐 경우 배열에 있는 모든 값을 두 배
    else:
        for i in range(N):
            B[i] //= 2
        cnt += 1

print(cnt)