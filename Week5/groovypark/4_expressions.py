# 숫자의 표현 Level 4
# 수학을 공부하던 민지는 재미있는 사실을 발견하였습니다. 그 사실은 바로 연속된 자연수의 합으로 어떤 숫자를 표현하는 방법이 여러 가지라는 것입니다. 예를 들어, 15를 표현하는 방법은
# (1+2+3+4+5)
# (4+5+6)
# (7+8)
# (15)
# 로 총 4가지가 존재합니다. 숫자를 입력받아 연속된 수로 표현하는 방법을 반환하는 expressions 함수를 만들어 민지를 도와주세요. 예를 들어 15가 입력된다면 4를 반환해 주면 됩니다.

def expressions(num):
    answer = 0
    for i in range(1, num+1):
        _sum = 0
        while _sum < num:
            _sum += i
            i += 1
        if _sum == num:
            answer += 1
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15));