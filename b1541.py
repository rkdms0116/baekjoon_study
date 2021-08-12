plus_num_list = list(map(str, input().split('-')))
min_sum = 0

for num_list in plus_num_list[0].split('+'):
    min_sum += int(num_list)

for num_list in plus_num_list[1:]:
    for num in map(int,num_list.split('+')):
        min_sum -= int(num)

print(min_sum)


# num_operations = input() # 숫자 연산을 받음
# oper = [] # 연산기호들('+' or '-')을 받음
# min_value_list = [] # 0004의 경우 4로 변환하기 위한 값들
# oper_index=[] # 연산 기호들의 인덱스 값

# for num in range(len(num_operations)):
#     if num_operations[num] == '+' or num_operations[num] == '-':
#         oper_index.append(num)
#     if num<num_operations.find('-') and num_operations[num] == '+':
#         oper.append('+')
#     elif num>=num_operations.find('-')>0 and (num_operations[num] == '+' or num_operations[num] == '-'): 
#         oper.append('-')

# min_value_list.append(int(num_operations[:oper_index[0]]))

# for i in range(len(oper)-1):
#     min_value_list.append(int(num_operations[oper_index[i]+1:oper_index[i+1]]))
# min_value_list.append(int(num_operations[oper_index[len(oper)-1]+1:]))


# result = ''
# for a in range(len(min_value_list)-1):
#     result += str(min_value_list[a]) +oper[a]
# result += str(min_value_list[len(min_value_list)-1])
# print(eval(result))  



# # 나중에 다시하자...^-^050+070
# # num_operation = input()
# # operation_list = []
# # for num in num_operation:
# #     if num == '+' or num == '-':
# #         operation_list.append(number)
# #     else:
# #         operation_list.append(num)
# # for i in range(0,len(operation_list)):
# #     if operation_list[i] == '+' and i > num_operation.find('-'):
# #         operation_list[i] = '-'

# # minimum_value = "".join(operation_list)
# # print(eval(minimum_value))