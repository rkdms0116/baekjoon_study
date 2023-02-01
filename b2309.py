from itertools import combinations

# 9명의 난쟁이들 키 받아오기
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

def find_seven(dwarfs):
    seven_dwarfs = combinations(dwarfs, 7)
    for dw in seven_dwarfs:
        if sum(dw) == 100:
            return sorted(list(dw))

for dwarf in find_seven(dwarfs):
    print(dwarf)