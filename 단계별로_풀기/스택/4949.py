# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    statement = input().rstrip()
    
    if statement == ".":
        break
    stack = []

    for s in statement:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")            