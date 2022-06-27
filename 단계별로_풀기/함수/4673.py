# 셀프 넘버
num_set = set()

def d(num):
    str_num = str(num)
    new_num = num
    for n in range(len(str_num)):
        new_num += int(str_num[n])
    if new_num < 10001:
        num_set.add(new_num)

for i in range(1, 10000):
    d(i)

for n in range(1, 10001):
    if n not in num_set:
        print(n)
