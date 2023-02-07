# # 성냥개비로 숫자를 나타낼 때 필요한 개수
# digit_num = [6,2,5,5,4,5,6,3,7,6]
# # 테스트 케이스의 개수
# N = int(input())
# # 성냥개비의 수
# for _ in range(N):
#     matchstick = int(input())

# 가장 작은 수
def min_digit(num):
    smallest_num = []
    q, r = divmod(num, 7)
# 이때, r이 1이면 q에서 까야지..
    if r == 1:
        q -= 1
        smallest_num.append(2)
        smallest_num.append(0)

# 7보다 작으면 digitnum에서 찾아서 돌려줌
    elif r == 2:
        smallest_num.append(1)
    elif r == 3:
        smallest_num.append(7)
    elif r == 4:
        smallest_num.append(4)
    elif r == 5:
        smallest_num.append(2)
    elif r == 6:
        if q == 0:
            return 6
        else:
            smallest_num.append(0)
# 7보다 크면 
    for _ in range(q):
        smallest_num.append(8) 
# 최소 숫자 만들기(0으로 시작하지 않는)
    smallest_num.sort()
    return smallest_num


# print(min_digit(3))
# print(min_digit(6))
# print(min_digit(7))
print(min_digit(15))

# 가장 큰 수
# 2,3개(숫자 1, 7)로 만들 수 있는 가장 큰 수  
def max_digit(num):
    largest_num = ''
    q, r = divmod(num, 2)
    if q>0 and r==1:
        largest_num += '7'
        largest_num += '1' * (q-1) 
    else:
        largest_num += '1' * q
    return int(largest_num)
