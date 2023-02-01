# 분해합
from itertools import product

# 한자리수 일 경우에는 N의 생성자는 N
def find(N):
    if len(str(N)) == 1:
        for n in range(10):
            if n+n == N:
                return n
        else:
            return 0
    else:
        # for n in range(len(str(N))-1, len(str(N))+1):
        #     for permu in product(list(i for i in range(10)), repeat = n-1):
        #         if int(str(N[0])-1) + ''.join(map(str, permu)) + sum(permu) == N:
        #             return int(''.join(map(str,permu)))
        # else:
        #     return 0
        for permu in product(list(i for i in range(10)), repeat = len(str(N))-1):
            num = int(str(N[0])-1) + ''.join(map(str, permu)) + sum(permu)
            
print(find(int(input())))