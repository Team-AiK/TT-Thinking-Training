def numberOfPrime(n):
    # 1부터 n사이의 소수는 몇 개인가요?
    total = 1
    for i in range(n+1) :
        for x in range(2,i): #2부터 i-1까지 나누어 본다
            if i % x == 0: #나누어 떨어지면 소수가 아니므로 break
                break
            elif x == i - 1: #i-1까지 나누어지지 않으면 소수
                total = total + 1
    return total


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(numberOfPrime(10))