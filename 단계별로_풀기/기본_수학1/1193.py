# 분수찾기

'''
X = int(input())

for n in range(1, 10**8):
    if n**2 + n >= 2*X:
        nth = n
        break
print(nth)
d = int(nth*(nth+1)/2) - X
print(f'{nth-d}/{1+d}')
'''

X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')