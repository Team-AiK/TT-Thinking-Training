def sum_digit(number):
    number = str(number)
    i = len(number)-1
    result = 0

    while i > -1:
      result += int(number[i])
      i = i - 1

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));