def solution(n):
    if n is 1:
        return 1
    elif n is 2:
        return 2
    else:
        n1 = 1
        n2 = 2
        temp = 0
        for i in range(n-2):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2%1000000007