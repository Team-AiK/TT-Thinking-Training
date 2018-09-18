def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    answer = []
    for i in range(n):
        # map1
        num1 = arr1[i]
        line = []
        # 라인 생성
        while True:
            if num1 % 2 == 0:
                line.append(' ')
            if num1 % 2 == 1:
                line.append('#')
            num1 = num1//2
            if num1 == 1:
                line.append('#')
                break
            if num1 == 0:
                break
        # 라인이 n보다 짧을 경우 
        while len(line) < n:
            line.append(' ')
        # 라인이 n보다 길 경우
        while len(line) > n:
            del line[0]
        # 맵에 라인 추가
        map1.append(line[::-1])
        # map1.append(''.join(line)[::-1])

        # map2
        num2 = arr2[i]
        line = []
        while True:
            if num2 % 2 == 0:
                line.append(' ')
            if num2 % 2 == 1:
                line.append('#')
            num2 = num2//2
            if num2 == 1:
                line.append('#')
                break
            if num2 == 0:
                break
        while len(line) < n:
            line.append(' ')
        while len(line) > n:
            del line[0]
        map2.append(line[::-1])

    # map1을 고치고 answer에 추가
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '#' or map2[i][j] == '#':
                map1[i][j] = '#'
        answer.append(''.join(map1[i]))
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))