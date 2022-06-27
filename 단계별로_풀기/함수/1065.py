# 한수
N = int(input())

cnt = 0
for n in range(1, N+1):
    if n < 100:
        cnt += 1
    # 세자리 이상
    else:
        N_str = str(n)
        if int(N_str[0]) - int(N_str[1]) == int(N_str[1]) - int(N_str[2]):
            cnt += 1

print(cnt)

def hansu(num):
    cnt = 0
    for n in range(1, num+1):
        if n < 100:
            cnt += 1
        else:
            N_str = str(n)
            if int(N_str[0]) - int(N_str[1]) == int(N_str[1]) - int(N_str[2]):
                cnt += 1
