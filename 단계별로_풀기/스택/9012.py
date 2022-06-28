# 괄호
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    is_vps = input().strip()
    test = 0
    for v in is_vps:
        if v == "(":
            test += 1
        else:
            if test > 0 :
                test -= 1
            else:
                print("NO")
                break
    else:
        if test:
            print("NO")
        else:
            print("YES")