def solution(n):
    fibo=[1,2]
    for i in range(2,n-1):
        fibo=[fibo[-1],fibo[0]+fibo[1]]
    return sum(fibo)%1000000007
