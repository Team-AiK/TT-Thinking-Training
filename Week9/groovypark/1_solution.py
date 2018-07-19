# N진수 게임

def solution1(n,t,m,p):
    i = 0
    answer = ""
    result = ""
    while(len(answer) < t*m):
        answer += str(convert(i,n))
        i += 1
    for x in range(t*m):
        if x % m == p - 1:
            result += answer[x]
        else:
            pass
    return result
        

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

print(solution1(2,4,2,1))
print(solution1(16,16,2,1))
print(solution1(16,16,2,2))