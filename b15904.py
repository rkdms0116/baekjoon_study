input_list = input()
answer = 'UCPC'
j = 0
for i in input_list:
    if i == answer[j]:
        j += 1
        if j == 4:
            break
if j == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')