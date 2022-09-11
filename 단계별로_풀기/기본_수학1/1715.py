# 손익분기점

# 고정 비용 A, 가변 비용 B, 노트북 가격 C
A, B, C = map(int, input().split())

n = 1
if B < C:
    # 알고리즘으로 > 시간초과
    # while True:
    #     if A + B*n < C*n:
    #         print(n)
    #         break
    #     else:
    #         n += 1
    # 바로 정답
    print(int(A/(C-B)+1))
else:
    print(-1)