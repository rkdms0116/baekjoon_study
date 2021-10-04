n = int(input())

# 예제
exam = []
for i in range(n):
    exam.append(int(input()))

# 저장될 stack
stack = []
# 정답 연산
oper = []
k = 0

for j in range(n):
    stack.append(j+1)
    oper.append('+')
    
    while k < n:
        try:
            if stack[-1] == exam[k]:
                stack.pop(-1)
                oper.append('-')
                k += 1
            else:
                break
        except IndexError:
            break

if stack:
    print('NO')
else:
    for i in range(len(oper)):
        print(oper[i])