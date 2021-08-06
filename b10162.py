a=300
b=60
c=10

T = int(input())
cnt = ''

cnt = str(T//a)+' '
T %= 300
cnt += str(T//b) +' '
T %= 60
cnt += str(T//c)
T %= 10

if T!=0 or T == '0 0 0':
    print(-1)
else:
    print(cnt)
