def collatz(num):
    
    answer = 0
    while True:
        if num==1:
            break
        elif answer ==500:
            answer=-1
            break
        elif num%2==0: #짝수
            num=num/2
        elif (num-1)%2==0:#홀수
            num=num*3+1
            
        answer+=1    
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(6))
