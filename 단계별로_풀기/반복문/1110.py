N = input()
cnt = 1
oldN = N 
def creatN(num):
    if len(num) == 1:
        nextNum = num + num
    else:
        sumNum = str(int(num[0]) + int(num[1]))
        nextNum = num[-1] + sumNum[-1]
    return nextNum

while int(creatN(oldN)) != int(N):
    cnt += 1
    oldN = creatN(oldN)

print(cnt)
