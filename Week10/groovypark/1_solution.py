def solution(n, m):
    answer = 0
    for i in range(n, m+1):
        if str(i) == str(i)[::-1]:
            answer += 1

    return answer
