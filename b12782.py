test_case = int(input())
for test in range(test_case):
    bin1, bin2 = map(str,input().split())
    
    # bin1, bin2의 차이를 level1에 넣어줍니다.
    bin1_cnt = bin1.count('1')
    bin2_cnt = bin2.count('1')
    fs_level1 = abs(bin1_cnt - bin2_cnt)

    # bin1, bin2 문자열 인덱스의 값이 다른 개수를 level2에 넣어줍니다.
    fs_level2 = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            fs_level2 += 1

    # 만약 level1=0이면 level2에서는 자리 이동이므로
    # 개수의 차이 /2 횟수 만큼 우정 레벨이 증가하게 됩니다.
    if fs_level1 == 0:
       fs_level = fs_level2//2
    else:   # 만약에 level1이 있을 경우. 인덱스 값의 차이에 1을 우선 넣어주게 되므로 차이의 
        fs_level = fs_level1 + (fs_level2-fs_level1)//2
            
    print(fs_level)

