
def Harshad(n):
    # n은 하샤드 수 인가요?
    number=n
    char=str(number)
    sum=0
    for a in char:
        sum+=int(a)
    if number%sum==0:
        return True
    return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
