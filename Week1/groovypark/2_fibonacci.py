def fibonacci(num):
    b = True
    f1 = 1
    f2 = 1

    while num > 2 :
        if b :
            f1 = f1 + f2
        else :
            f2 = f1 + f2

        b = not b
        num -= 1

    if b :
        return f2
    else :
        return f1
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))