import sys, time
input = sys.stdin.readline

def check_VPS(test_VPS):
    # 만약에 test_VPS length가 홀수라면 무조건 VPS return 'NO'
    if len(test_VPS)% 2:
        return 'NO'
    # 짝수라면 test 시작
    else:
        VPS = 0
        for test in test_VPS:
            if test == '(':
                VPS += 1

            else:
                # VPS에서 '(' 없는데 ')' 시도 시 return 'NO'
                if VPS == 0:
                    return 'NO'
                else:
                    VPS -= 1
                    
        # 남아있는 VPS 속 '(' 개수가 없다면 pair가 맞음
        if VPS == 0:
            return 'YES'
        else:
            return 'NO'


T = int(input())
start = time.time()

for t in range(T):
    my_VPS = input().strip()
    result = check_VPS(my_VPS)
    print(result)

print("time : ", time.time() - start)
