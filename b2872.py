import sys

book_num = int(input())
book_list =[int(sys.stdin.readline())]
max_num = book_list[0]

for i in range(1,book_num):
    book_list.append(int(sys.stdin.readline()))

cnt = book_num-1
for i in range(book_num,-1,-1):
    if book_list.index(i-1) < book_list.index(i):
        cnt -= 1
    else:
        break
print(cnt)