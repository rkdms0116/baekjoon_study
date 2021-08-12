N, k = map(int, input().split())
money_list = []
for _ in range(N):
    money_list.append(int(input()))

money_cnt = 0
for i in range(N-1,-1,-1):  # 큰 숫자부터 나누어 보기로 합니다
    while k //money_list[i] >0:  # 몫이 0보다 클 때까지만 나누어 보기로 합니다.
        quo = k//money_list[i]
        money_cnt += quo
        k -= money_list[i]*quo

print(money_cnt)