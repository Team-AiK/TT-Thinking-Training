def getMinSum(A,B):
    answer = 0
    size=len(A)
    while size > 0:
        num1=min(A)
        A.remove(num1)
        num2=max(B)
        B.remove(num2)
        size-=1
        answer+=num1*num2
    return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1,2],[3,4]))
