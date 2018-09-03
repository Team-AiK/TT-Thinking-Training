def solution(no, works):
    result = 0
    while(no > 0):
        works.sort(reverse=True)
        works[0] -= 1
        no -= 1
    for i in works:
        result += i**2
    return result

# 케이스 7,8 틀림