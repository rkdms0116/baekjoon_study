N = int(input())

city = []
for _ in range(N):
    city.append(list(int(char) for char in input()))

delta = [[1,0],[0,1],[-1,0],[0,-1]]

danji = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if city[i][j] == 1:
            city[i][j] = 0
            danji += 1
            for k in range(4):
                x = i + delta[k][0]
                y = j + delta[k][1]
                if city[x][y] == 1:
                    cnt += 1
                    city[x][y] = 0