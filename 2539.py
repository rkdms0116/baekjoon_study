N = int(input())

find_min_list = []
a = N//5

while a >= 0:
    if (N-a*5)%3 ==0:
        find_min_list.append(a+(N-a*5)//3)
    a -=1

if find_min_list ==[]:
    print('-1')
else:
    print(min(find_min_list))