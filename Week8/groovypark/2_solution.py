def solution(n, money):
    answer = 0
    dp = [0 for i in range(n+1)]
    
    for i in range(n+1):
        if i % money[0] == 0:
            dp[i] = 1
        else:
            dp[i] = 0
    for i in range(1,len(money)):
        for j in range(money[i],n+1):
            dp[j] += dp[j-money[i]]
            
    answer = dp[n] % 1000000007
    return answer